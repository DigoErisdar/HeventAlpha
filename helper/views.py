import operator
from functools import reduce

from django.contrib.postgres.search import SearchVector, TrigramSimilarity
from django.db.models import Q
from django.http import JsonResponse
from rest_framework.generics import ListAPIView


class AjaxFormMixin:
    """
    Обрабатывает формы через ajax
    :param success_message: str Сообщение сохранения
    :param success_redirect: str Ссылка на перенаправление
    :param form_save: bool Нужно ли сохранять форму
    """
    success_message = 'Изменения сохранены'
    success_redirect = None
    form_save = True

    def form_invalid(self, form):
        return JsonResponse({"fields": form.errors, "errors": True})

    def form_valid(self, form):
        if self.form_save:
            form.save()
        data = {
            "error": False
        }
        if self.success_redirect or form.cleaned_data.get('next'):
            data['redirect'] = form.cleaned_data.get('next') or self.success_redirect
        else:
            data['message'] = self.success_message
        return JsonResponse(data)


class HeventViewMixin:
    title = None

    def get_context_data(self, **kwargs):
        context = super(HeventViewMixin, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context


class SearchAPIView(ListAPIView):
    def __init__(self, *args, **kwargs):
        super(SearchAPIView, self).__init__(*args, **kwargs)
        self.vector_fields.append(self.search_field)
        self.vector_fields = list(set(self.vector_fields))

    vector_fields = []
    search_field = ''
    user_id_field = None

    def _get_search_words(self, search):
        search = search.lower()
        alph_en = list("qwertyuiop[]asdfghjkl;'zxcvbnm,.")
        alph_ru = list("йцукенгшщзхъфывапролджэячсмитьбю")
        word_ru, word_en = '', ''
        for word in search:
            if word in alph_en:
                word_en += word
                word_ru += alph_ru[alph_en.index(word)]
            elif word in alph_ru:
                word_ru += word
                word_en += alph_en[alph_ru.index(word)]
            else:
                word_ru += ' '
                word_en += ' '
        return word_ru, word_en

    def _search_query(self, qs, search, config='russian'):
        search_vector = SearchVector(*self.vector_fields, config=config)
        annotate = {
            'search': search_vector,
            'similarity': TrigramSimilarity(self.search_field, search)
        }
        return qs.annotate(**annotate).filter(Q(similarity__gt=0.1) | Q(search=search))

    def get_queryset(self):
        qs = super(SearchAPIView, self).get_queryset()
        search = self.request.GET.get('search', None)
        if search:
            ru, en = self._get_search_words(search.lower())
            qs = self._search_query(qs, ru, 'russian') or self._search_query(qs, en, 'english')
            qs = self.serializer_class.Meta.model.objects.filter(id__in=list(qs.values_list('id', flat=True)))

        filters = {}

        my = self.request.GET.get('my', 0)
        if my == str(1) and self.user_id_field:
            filters[self.user_id_field] = self.request.user.id
        ids = self.request.GET.get('ids', None)
        if ids:
            filters['id__in'] = ids.split(',')

        return qs.filter(**filters)


class ServerFilterMixin:
    def get_queryset(self):
        qs = super(ServerFilterMixin, self).get_queryset()
        filters = {}
        servers = self.request.GET.get('server', False)
        if servers:
            servers = servers.split(',')
            if len(servers) == len([server for server in servers if server.isdigit()]):
                filters['server_id__in'] = servers
            else:
                qs = qs.filter(reduce(operator.or_, (Q(server__title__icontains=server) for server in servers)))
        return qs.filter(**filters)