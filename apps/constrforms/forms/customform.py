from django import forms

from apps.chars.models import Char
from apps.constrforms.choices import CHOICE_FIELD
from apps.constrforms.models import FormField, Claim


class CustomFormForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.form = kwargs.pop('custom_form')
        self.user = kwargs.pop('user')
        self.server = kwargs.pop('server')
        super(CustomFormForm, self).__init__(*args, **kwargs)
        self.fields['char'] = forms.ModelChoiceField(
            label='Персонаж', help_text='От чьего лица будет написана заявка',
            queryset=Char.objects.filter(user=self.user, server=self.server), required=True,
            widget=forms.Select(attrs={'class': 'form-control'})
        )
        for formfield in FormField.objects.select_related('field').filter(form=self.form).iterator():
            field = formfield.field
            default_field_values = {'label': field.label, 'help_text': field.help_text, 'required': field.required}
            if field.type == 'int':
                custom_field = forms.IntegerField(**default_field_values,
                                                  min_value=field.integerfield.min, max_value=field.integerfield.max)
            elif field.type == 'img':
                custom_field = forms.ImageField(**default_field_values)
            elif field.type == 'choice':
                type = field.choicefield.widget
                choices = field.choicefield.choices.values_list()
                if type in CHOICE_FIELD.keys():
                    custom_field = forms.ChoiceField(**default_field_values, choices=choices)
                else:
                    custom_field = forms.MultipleChoiceField(**default_field_values, choices=choices)
                if type == 'radio':
                    custom_field.widget = forms.RadioSelect(choices=choices)
                elif type == 'checkbox':
                    custom_field.widget = forms.CheckboxSelectMultiple(choices=choices)
            else:
                custom_field = forms.CharField(**default_field_values)
            field_name = 'field-' + str(formfield.pk)
            self.fields[field_name] = custom_field
            if not( field.type == 'choice' and field.choicefield.widget in ['radio', 'checkbox']):
                self.fields[field_name].widget.attrs = {'class': 'form-control'}
            self.base_fields[field_name] = custom_field

    def get_text(self):
        text = '<ol>'
        for field, value in self.cleaned_data.items():
            if field != 'char' and value:
                text += f"<li>{field} {value}</li>"
        text += '</ol>'
        return text

    def save(self):
        char = self.cleaned_data.get('char')
        text = self.get_text()
        request = Claim.objects.create(char=char, text=text, form=self.form)
        return request.get_absolute_url()

    def clean(self):
        data = {'char': self.cleaned_data.get('char')}
        for name, field in self.fields.items():
            if name != 'char':
                if hasattr(field, 'choices'):
                    choices = {str(key): value for key, value in field.choices}
                    key = self.cleaned_data.get(name, '-')
                    if isinstance(key, list):
                        value = ', '.join([choices.get(str(k)) for k in key if choices.get(str(k))])
                    else:
                        value = choices.get(str(key), '-')
                    data[field.label] = value
                else:
                    data[field.label] = self.cleaned_data.get(name, '-')
        return data
