# encoding: utf-8
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        for qde_xtf in orm['xtf.QualifiedDublinCoreElement'].objects.all().order_by('id'):
            qde = orm.QualifiedDublinCoreElement()
            qde.content = qde_xtf.content
            qde.term = qde_xtf.term
            qde.qualifier = qde_xtf.qualifier
            #import pdb;pdb.set_trace()
            c= orm['contenttypes.ContentType'].objects.get(pk=qde_xtf.content_type.pk)
            #c.name = qde_xtf.content_type.name
            #c.app_label = qde_xtf.content_type.app_label
            #c.model = qde_xtf.content_type.model
            qde.content_type = c
            #qde.content_type = qde_xtf.content_type
            qde.object_id = qde_xtf.object_id
            qde.save()
        for qdeh_xtf in  orm['xtf.QualifiedDublinCoreElementHistory'].objects.all().order_by('id'):
            qdeh = orm.QualifiedDublinCoreElementHistory()
            qdeh.content = qdeh_xtf.content
            qdeh.term = qdeh_xtf.term
            qdeh.qualifier = qdeh_xtf.qualifier
            c= orm['contenttypes.ContentType'].objects.get(pk=qdeh_xtf.content_type.pk)
            #c.name = qdeh_xtf.content_type.name
            #c.app_label = qdeh_xtf.content_type.app_label
            #c.model = qdeh_xtf.content_type.model
            qdeh.content_type = c
            #qdeh.content_type = qdeh_xtf.content_type
            qdeh.object_id = qdeh_xtf.object_id
            qdeh.qdce = orm['DublinCore.QualifiedDublinCoreElement'].objects.get(pk=qdeh_xtf.qdce.pk)
            qdeh.qdce_id_stored = qdeh_xtf.qdce_id_stored
            qdeh.save()
            


    def backwards(self, orm):
        "Write your backwards methods here."


    models = {
        'DublinCore.qualifieddublincoreelement': {
            'Meta': {'ordering': "['term']", 'object_name': 'QualifiedDublinCoreElement'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'qualifier': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'term': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'DublinCore.qualifieddublincoreelementhistory': {
            'Meta': {'ordering': "['term']", 'object_name': 'QualifiedDublinCoreElementHistory'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'qdce': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'history'", 'null': 'True', 'to': "orm['DublinCore.QualifiedDublinCoreElement']"}),
            'qdce_id_stored': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'qualifier': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'term': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'xtf.arkeditrequest': {
            'Meta': {'object_name': 'ARKEditRequest'},
            'action_taken': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'ark': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'content_new': ('django.db.models.fields.TextField', [], {}),
            'content_old': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'delete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'element': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'qualifier_new': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'qualifier_old': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'xtf.arkobject': {
            'Meta': {'object_name': 'ARKObject'},
            'ark': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_db': ('xtf.models.ImageLinkField', [], {'null': 'True', 'blank': 'True'}),
            'thumbnail_db': ('xtf.models.ImageLinkField', [], {'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'xtf.arkset': {
            'Meta': {'object_name': 'ARKSet'},
            'ark_objects': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['xtf.ARKObject']", 'through': "orm['xtf.ARKSetMember']", 'symmetrical': 'False'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'markup': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'xtf.arksetmember': {
            'Meta': {'unique_together': "(('set', 'object'),)", 'object_name': 'ARKSetMember'},
            'annotation': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['xtf.ARKObject']"}),
            'set': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['xtf.ARKSet']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'xtf.geopoint': {
            'Meta': {'unique_together': "(('object_id', 'content_type'),)", 'object_name': 'GeoPoint'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'exact': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'default': '37.808690599999998'}),
            'lon': ('django.db.models.fields.FloatField', [], {'default': '-122.2675416'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'xtf.qualifieddublincoreelement': {
            'Meta': {'ordering': "['term']", 'object_name': 'QualifiedDublinCoreElement'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'xtfqdc'", 'to': "orm['contenttypes.ContentType']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'qualifier': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'term': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'xtf.qualifieddublincoreelementhistory': {
            'Meta': {'ordering': "['term']", 'object_name': 'QualifiedDublinCoreElementHistory'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'xtfqdchist'", 'to': "orm['contenttypes.ContentType']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'qdce': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'history'", 'null': 'True', 'to': "orm['xtf.QualifiedDublinCoreElement']"}),
            'qdce_id_stored': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'qualifier': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'term': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['xtf', 'DublinCore']
