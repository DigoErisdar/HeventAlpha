from rest_framework import serializers

from apps.pw.models import Server, Rase
from helper.serializers import ChooseFields


class ServerSerializer(ChooseFields, serializers.ModelSerializer):
    class Meta:
        model = Server
        exclude = ()


class RaseSerializer(ChooseFields, serializers.ModelSerializer):

    class Meta:
        model = Rase
        exclude = ()
