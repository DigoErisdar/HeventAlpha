
class ChooseFields:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.context.get('request'):
            fields = self.context['request'].query_params.get('fields')
            if fields:
                fields = fields.split(',')
                allowed = set(fields)
                existing = set(self.fields.keys())
                if allowed & existing:
                    for field_name in existing - allowed:
                        self.fields.pop(field_name)

class DynamicSerializerMixin:

    def __init__(self, *args, **kwargs):
        fields = kwargs.pop("fields", None)
        excluded_fields = kwargs.pop("excluded_fields", None)
        required_fields = kwargs.pop("required_fields", None)

        super().__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

            if isinstance(fields, dict):
                for field, config in fields.items():
                    setattr(self.fields[field], config)

        if excluded_fields is not None:
            for field_name in excluded_fields:
                self.fields.pop(field_name)

        if required_fields is not None:
            for field_name in required_fields:
                self.fields[field_name].required = True
