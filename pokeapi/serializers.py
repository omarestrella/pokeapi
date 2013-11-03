from rest_framework import serializers, fields

from pokeapi import models


class PokemonSerializer(serializers.ModelSerializer):
    types = serializers.RelatedField(many=True)

    class Meta:
        model = models.Pokemon
        fields = ('name', 'types')
