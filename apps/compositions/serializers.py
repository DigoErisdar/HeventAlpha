from django.conf import settings
from rest_framework import serializers
from apps.compositions.models import Composition, Rank, Soklan
from apps.chars.serializers import CharSerializer
from helper.serializers import DynamicSerializerMixin


class RankSerializer(DynamicSerializerMixin, serializers.ModelSerializer):
    title_display = serializers.SerializerMethodField('get_title_display')

    class Meta:
        model = Rank
        exclude = ()

    def get_title_display(self, obj):
        return obj.get_title_display()


class CompositionSerializer(DynamicSerializerMixin, serializers.ModelSerializer):

    class Meta:
        model = Composition
        exclude = ()


class SoklanSerializer(serializers.ModelSerializer):

    date_joined = serializers.DateTimeField(format=settings.DATETIME_FORMAT)
    rank = RankSerializer(fields=['id', 'title', 'title_display'])
    composition = CompositionSerializer(fields=['id', 'title'])
    char = CharSerializer(fields=['nickname', 'rase'])

    class Meta:
        model = Soklan
        exclude = ('permissions', )
