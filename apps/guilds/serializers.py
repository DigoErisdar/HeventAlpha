from rest_framework import serializers
from apps.guilds.models import Guild, Profile
from apps.pw.serializers import ServerSerializer
from helper.serializers import ChooseFields


class GuildProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        exclude = ('guild',)


class GuildSerializer(ChooseFields, serializers.ModelSerializer):
    server = ServerSerializer()
    profile = GuildProfileSerializer()
    url = serializers.URLField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Guild
        exclude = ('schema_name',)
