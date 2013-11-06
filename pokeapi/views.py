from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from pokeapi import models, serializers


class PokemonViewSet(ModelViewSet):
    model = models.Pokemon
    serializer_class = serializers.PokemonSerializer
    filter_backends = (filters.SearchFilter, filters.DjangoFilterBackend)
    search_fields = ('name',)
    filter_fields = ('name', 'types')

