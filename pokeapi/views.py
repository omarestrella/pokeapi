from rest_framework.viewsets import ModelViewSet

from pokeapi import models, serializers


class PokemonViewSet(ModelViewSet):
    model = models.Pokemon
    serializer_class = serializers.PokemonSerializer

