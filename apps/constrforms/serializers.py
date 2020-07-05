from rest_framework import serializers

from apps.chars.serializers import CharSerializer
from apps.constrforms.models import CustomForm, Claim, RequestPage, RequestStatus, \
    Field, FormField, TextField, IntegerField, ChoiceField, ImageField, ChoicesForField
from helper.serializers import DynamicSerializerMixin


class TextFieldSerializer(DynamicSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = TextField
        exclude = ('id', 'label', 'help_text', 'required', 'type',)


class IntegerFieldSerializer(DynamicSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = IntegerField
        exclude = ('id', 'label', 'help_text', 'required', 'type',)


class ChoiceSerializer(DynamicSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = ChoicesForField
        exclude = ()


class ChoiceFieldSerializer(DynamicSerializerMixin, serializers.ModelSerializer):
    widget_display = serializers.SerializerMethodField()
    choices = ChoiceSerializer(many=True)

    class Meta:
        model = ChoiceField
        exclude = ('id', 'label', 'help_text', 'required', 'type',)

    def get_widget_display(self, obj):
        return obj.get_widget_display()


class FieldSerializer(serializers.ModelSerializer):
    extra = serializers.SerializerMethodField()

    class Meta:
        model = Field
        exclude = ()

    def get_extra(self, obj):
        if hasattr(obj, 'integerfield'):
            return IntegerFieldSerializer(instance=obj.integerfield).data
        elif hasattr(obj, 'choicefield'):
            return ChoiceFieldSerializer(instance=obj.choicefield).data
        elif hasattr(obj, 'textfield'):
            return TextFieldSerializer(instance=obj.textfield).data
        else:
            return None


class FormFieldSerializer(serializers.ModelSerializer):
    field = FieldSerializer()

    class Meta:
        model = FormField
        exclude = ('form', )


class RequestStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestStatus
        exclude = ('form',)


class FormSerializer(serializers.ModelSerializer):
    default_status = RequestStatusSerializer()
    statuses = RequestStatusSerializer(many=True)
    fields = FormFieldSerializer(many=True)

    class Meta:
        model = CustomForm
        exclude = ()


class PageSerializer(serializers.ModelSerializer):
    url = serializers.URLField(source='get_absolute_url', read_only=True)
    form = FormSerializer()

    class Meta:
        model = RequestPage
        exclude = ()


class ClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Claim
        exclude = ()
