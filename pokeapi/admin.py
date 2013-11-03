from django.contrib import admin

from pokeapi import models


admin.site.register(models.Type)
admin.site.register(models.Pokemon)
