from django import forms
from django.utils.dates import WEEKDAYS

from apps.compositions.models import Composition


class CompositionAdminForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CompositionAdminForm, self).__init__(*args, **kwargs)
        self.fields['close_loot'] = forms.MultipleChoiceField(label="КХ лут закрыт в", choices=tuple(WEEKDAYS.items()),
                                                              widget=forms.SelectMultiple(), required=False)

    class Meta:
        model = Composition
        exclude = []