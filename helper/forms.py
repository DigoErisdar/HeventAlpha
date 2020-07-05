from django import forms


# Добавляет бутстраповские классы для полей формы
class BootstrapForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(BootstrapForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            cls = field.widget.attrs.get('class', '')
            cls = cls.split(' ')
            if field.__class__.__name__ not in ['BooleanField'] \
                    and field.widget.__class__.__name__ not in ['RadioSelect']:
                cls += ['form-control']
            if field.widget.__class__.__name__ == 'Select':
                cls += ['selectpicker']
            if field.__class__.__name__ == 'DateField':
                cls += ['dateinput']
                field.widget.attrs['autocomplete'] = 'off'
            if field.widget.__class__.__name__ == 'RadioSelect':
                cls += ['hor-radio']
            field.widget.attrs['class'] = ' '.join(cls)
