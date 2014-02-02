# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Carro'
        db.delete_table(u'carros_carro')

        # Adding model 'modelos'
        db.create_table(u'carros_modelos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modelo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('marca', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['carros.marcas'])),
        ))
        db.send_create_signal(u'carros', ['modelos'])

        # Adding model 'marcas'
        db.create_table(u'carros_marcas', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('marca', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'carros', ['marcas'])

        # Adding model 'carros'
        db.create_table(u'carros_carros', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('veiculo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('modelo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['carros.modelos'])),
            ('preco', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
        ))
        db.send_create_signal(u'carros', ['carros'])


    def backwards(self, orm):
        # Adding model 'Carro'
        db.create_table(u'carros_carro', (
            ('marca', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('preco', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('modelo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('veiculo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'carros', ['Carro'])

        # Deleting model 'modelos'
        db.delete_table(u'carros_modelos')

        # Deleting model 'marcas'
        db.delete_table(u'carros_marcas')

        # Deleting model 'carros'
        db.delete_table(u'carros_carros')


    models = {
        u'carros.carros': {
            'Meta': {'object_name': 'carros'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modelo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['carros.modelos']"}),
            'preco': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'veiculo': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'carros.marcas': {
            'Meta': {'object_name': 'marcas'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marca': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'carros.modelos': {
            'Meta': {'object_name': 'modelos'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marca': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['carros.marcas']"}),
            'modelo': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['carros']