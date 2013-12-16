# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'modelos'
        db.delete_table(u'carros_modelos')

        # Deleting model 'marcas'
        db.delete_table(u'carros_marcas')

        # Deleting model 'carros'
        db.delete_table(u'carros_carros')

        # Adding model 'Marca'
        db.create_table(u'carros_marca', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('marca', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'carros', ['Marca'])

        # Adding model 'Veiculo'
        db.create_table(u'carros_veiculo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('veiculo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('modelo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['carros.Modelo'])),
            ('preco', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
        ))
        db.send_create_signal(u'carros', ['Veiculo'])

        # Adding model 'Modelo'
        db.create_table(u'carros_modelo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modelo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('marca', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['carros.Marca'])),
        ))
        db.send_create_signal(u'carros', ['Modelo'])


    def backwards(self, orm):
        # Adding model 'modelos'
        db.create_table(u'carros_modelos', (
            ('modelo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
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
            ('preco', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('veiculo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('modelo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['carros.modelos'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'carros', ['carros'])

        # Deleting model 'Marca'
        db.delete_table(u'carros_marca')

        # Deleting model 'Veiculo'
        db.delete_table(u'carros_veiculo')

        # Deleting model 'Modelo'
        db.delete_table(u'carros_modelo')


    models = {
        u'carros.marca': {
            'Meta': {'object_name': 'Marca'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marca': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'carros.modelo': {
            'Meta': {'object_name': 'Modelo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marca': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['carros.Marca']"}),
            'modelo': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'carros.veiculo': {
            'Meta': {'object_name': 'Veiculo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modelo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['carros.Modelo']"}),
            'preco': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'veiculo': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['carros']