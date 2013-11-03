# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field type on 'Pokemon'
        db.delete_table(db.shorten_name(u'pokeapi_pokemon_type'))

        # Adding M2M table for field types on 'Pokemon'
        m2m_table_name = db.shorten_name(u'pokeapi_pokemon_types')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pokemon', models.ForeignKey(orm[u'pokeapi.pokemon'], null=False)),
            ('type', models.ForeignKey(orm[u'pokeapi.type'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pokemon_id', 'type_id'])


    def backwards(self, orm):
        # Adding M2M table for field type on 'Pokemon'
        m2m_table_name = db.shorten_name(u'pokeapi_pokemon_type')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pokemon', models.ForeignKey(orm[u'pokeapi.pokemon'], null=False)),
            ('type', models.ForeignKey(orm[u'pokeapi.type'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pokemon_id', 'type_id'])

        # Removing M2M table for field types on 'Pokemon'
        db.delete_table(db.shorten_name(u'pokeapi_pokemon_types'))


    models = {
        u'pokeapi.pokemon': {
            'Meta': {'object_name': 'Pokemon'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'types': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['pokeapi.Type']", 'symmetrical': 'False'})
        },
        u'pokeapi.type': {
            'Meta': {'object_name': 'Type'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['pokeapi']