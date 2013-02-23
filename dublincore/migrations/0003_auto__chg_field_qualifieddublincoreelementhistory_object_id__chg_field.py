# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'QualifiedDublinCoreElementHistory.object_id'
        db.alter_column('DublinCore_qualifieddublincoreelementhistory', 'object_id', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'QualifiedDublinCoreElement.object_id'
        db.alter_column('DublinCore_qualifieddublincoreelement', 'object_id', self.gf('django.db.models.fields.CharField')(max_length=255))


    def backwards(self, orm):
        
        # Changing field 'QualifiedDublinCoreElementHistory.object_id'
        db.alter_column('DublinCore_qualifieddublincoreelementhistory', 'object_id', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'QualifiedDublinCoreElement.object_id'
        db.alter_column('DublinCore_qualifieddublincoreelement', 'object_id', self.gf('django.db.models.fields.PositiveIntegerField')())


    models = {
        'DublinCore.qualifieddublincoreelement': {
            'Meta': {'ordering': "['term']", 'object_name': 'QualifiedDublinCoreElement'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
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
            'object_id': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'qdce': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'history'", 'null': 'True', 'to': "orm['DublinCore.QualifiedDublinCoreElement']"}),
            'qdce_id_stored': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'qualifier': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'term': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['DublinCore']
