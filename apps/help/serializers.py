from rest_framework import serializers
from apps.help.models import FeedBack


class FeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBack
        exclude = ()
