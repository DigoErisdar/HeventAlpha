from rest_framework import serializers

from apps.chars.models import Char
from apps.pw.serializers import ServerSerializer, RaseSerializer
from apps.guilds.serializers import GuildSerializer
from helper.serializers import DynamicSerializerMixin


class CharSerializer(DynamicSerializerMixin, serializers.ModelSerializer):
    guild = GuildSerializer()
    server = ServerSerializer()
    rase = RaseSerializer()

    class Meta:
        model = Char
        exclude = ('user',)
