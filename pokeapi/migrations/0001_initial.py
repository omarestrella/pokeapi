# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Type'
        db.create_table(u'pokeapi_type', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=6)),
        ))
        db.send_create_signal(u'pokeapi', ['Type'])

        # Adding model 'Pokemon'
        db.create_table(u'pokeapi_pokemon', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'pokeapi', ['Pokemon'])

        # Adding M2M table for field type on 'Pokemon'
        m2m_table_name = db.shorten_name(u'pokeapi_pokemon_type')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('pokemon', models.ForeignKey(orm[u'pokeapi.pokemon'], null=False)),
            ('type', models.ForeignKey(orm[u'pokeapi.type'], null=False))
        ))
        db.create_unique(m2m_table_name, ['pokemon_id', 'type_id'])


    def backwards(self, orm):
        # Deleting model 'Type'
        db.delete_table(u'pokeapi_type')

        # Deleting model 'Pokemon'
        db.delete_table(u'pokeapi_pokemon')

        # Removing M2M table for field type on 'Pokemon'
        db.delete_table(db.shorten_name(u'pokeapi_pokemon_type'))


    models = {
        u'pokeapi.pokemon': {
            'Meta': {'object_name': 'Pokemon'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['pokeapi.Type']", 'symmetrical': 'False'})
        },
        u'pokeapi.type': {
            'Meta': {'object_name': 'Type'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['pokeapi']