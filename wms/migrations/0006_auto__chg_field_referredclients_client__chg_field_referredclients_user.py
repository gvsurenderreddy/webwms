# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'ReferredClients.client'
        db.alter_column('wms_referredclients', 'client_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wms.Client']))

        # Changing field 'ReferredClients.user'
        db.alter_column('wms_referredclients', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

    def backwards(self, orm):

        # Changing field 'ReferredClients.client'
        db.alter_column('wms_referredclients', 'client_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

        # Changing field 'ReferredClients.user'
        db.alter_column('wms_referredclients', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wms.Client']))

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'to': "orm['auth.Group']", 'blank': 'True', 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_set'", 'to': "orm['auth.Permission']", 'blank': 'True', 'symmetrical': 'False'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'ordering': "('name',)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'wms.client': {
            'Meta': {'object_name': 'Client'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_holder': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'wms_id': ('django.db.models.fields.IntegerField', [], {})
        },
        'wms.incoming': {
            'Meta': {'object_name': 'Incoming'},
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'holder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wms.Client']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'wms.incomingdetail': {
            'Meta': {'object_name': 'IncomingDetail'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inc': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wms.Incoming']"}),
            'sku': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wms.Sku']"}),
            'units': ('django.db.models.fields.IntegerField', [], {})
        },
        'wms.order': {
            'Meta': {'object_name': 'Order'},
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'holder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wms.Client']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'wms.orderdetail': {
            'Meta': {'object_name': 'OrderDetail'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wms.Order']"}),
            'sku': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wms.Sku']"}),
            'units': ('django.db.models.fields.IntegerField', [], {})
        },
        'wms.referredclients': {
            'Meta': {'object_name': 'ReferredClients'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wms.Client']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'wms.sku': {
            'Meta': {'object_name': 'Sku'},
            'holder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wms.Client']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sku_id': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['wms']