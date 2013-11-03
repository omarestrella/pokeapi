from django.db import models


TYPE_CHOICES = (
    ('normal', 'Normal'),
    ('fighting', 'Fighting'),
    ('flying', 'Flying'),
    ('poison', 'Poison'),
    ('ground', 'Ground'),
    ('rock', 'Rock'),
    ('bug', 'Bug'),
    ('ghost', 'Ghost'),
    ('steel', 'Steel'),
    ('fire', 'Fire'),
    ('water', 'Water'),
    ('grass', 'Grass'),
    ('electric', 'Electric'),
    ('psychic', 'Psychic'),
    ('ice', 'Ice'),
    ('dragon', 'Dragon'),
    ('dark', 'Dark'),
    ('fairy', 'Fairy')
)


class Type(models.Model):
    name = models.CharField(max_length=255, unique=True)
    color = models.CharField(max_length=6)

    def __unicode__(self):
        return u'%s' % self.name.capitalize()


class Pokemon(models.Model):
    name = models.CharField(max_length=255)
    types = models.ManyToManyField(Type)

    def __unicode__(self):
        return u'%s' % self.name

    class Meta:
        ordering = ['name']
