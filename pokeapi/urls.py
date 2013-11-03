from rest_framework.routers import DefaultRouter

from pokeapi import views

router = DefaultRouter()
router.register(r'pokemon', views.PokemonViewSet)
urlpatterns = router.urls
