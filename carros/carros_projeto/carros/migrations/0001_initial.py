# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Carro'
        db.create_table(u'carros_carro', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('marca', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('modelo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('veiculo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('preco', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
        ))
        db.send_create_signal(u'carros', ['Carro'])


    def backwards(self, orm):
        # Deleting model 'Carro'
        db.delete_table(u'carros_carro')


    models = {
        u'carros.carro': {
            'Meta': {'object_name': 'Carro'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marca': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'modelo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'preco': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'veiculo': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['carros']