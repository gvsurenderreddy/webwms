# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Payment'
        db.create_table('wms_payment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=11, decimal_places=4)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('wms', ['Payment'])


    def backwards(self, orm):
        # Deleting model 'Payment'
        db.delete_table('wms_payment')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'})
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'user_set'", 'to': "orm['auth.Group']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'user_set'", 'to': "orm['auth.Permission']", 'blank': 'True'}),
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
            'Meta': {'managed': 'False', 'object_name': 'Client', 'db_table': "'web_client'"},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sdid': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'wms.incoming': {
            'Meta': {'managed': 'False', 'object_name': 'Incoming', 'db_table': "'web_incoming'"},
            'client_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'date_to_ship': ('django.db.models.fields.DateTimeField', [], {}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'holder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wms.Client']"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'sdid': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'wms.incomingdetail': {
            'Meta': {'managed': 'False', 'object_name': 'IncomingDetail', 'db_table': "'web_incoming_detail'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'incoming': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wms.Order']"}),
            'line': ('django.db.models.fields.IntegerField', [], {}),
            'qty': ('django.db.models.fields.IntegerField', [], {}),
            'received': ('django.db.models.fields.IntegerField', [], {}),
            'sku': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wms.Sku']"}),
            'sku_name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'wms.order': {
            'Meta': {'managed': 'False', 'object_name': 'Order', 'db_table': "'web_order'"},
            'client_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'date_to_ship': ('django.db.models.fields.DateTimeField', [], {}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'holder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wms.Client']"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'sdid': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'wms.orderdetail': {
            'Meta': {'managed': 'False', 'object_name': 'OrderDetail', 'db_table': "'web_order_detail'"},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'line': ('django.db.models.fields.IntegerField', [], {}),
            'moved': ('django.db.models.fields.IntegerField', [], {}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wms.Order']"}),
            'packed': ('django.db.models.fields.IntegerField', [], {}),
            'planned': ('django.db.models.fields.IntegerField', [], {}),
            'qty': ('django.db.models.fields.IntegerField', [], {}),
            'shiped': ('django.db.models.fields.IntegerField', [], {}),
            'sku': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wms.Sku']"}),
            'sku_name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'wms.payment': {
            'Meta': {'object_name': 'Payment'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '4'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'wms.referredclients': {
            'Meta': {'managed': 'False', 'object_name': 'ReferredClients'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wms.Client']"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'wms.sku': {
            'Meta': {'managed': 'False', 'object_name': 'Sku', 'db_table': "'web_sku'"},
            'holder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wms.Client']"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sdid': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sku_id': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['wms']