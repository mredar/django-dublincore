# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'QualifiedDublinCoreElement'
        db.create_table('DublinCore_qualifieddublincoreelement', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('term', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('qualifier', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('DublinCore', ['QualifiedDublinCoreElement'])

        # Adding model 'QualifiedDublinCoreElementHistory'
        db.create_table('DublinCore_qualifieddublincoreelementhistory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('object_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('content_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'])),
            ('term', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('qualifier', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('qdce', self.gf('django.db.models.fields.related.ForeignKey')(related_name='history', null=True, to=orm['DublinCore.QualifiedDublinCoreElement'])),
            ('qdce_id_stored', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal('DublinCore', ['QualifiedDublinCoreElementHistory'])


    def backwards(self, orm):
        
        # Deleting model 'QualifiedDublinCoreElement'
        db.delete_table('DublinCore_qualifieddublincoreelement')

        # Deleting model 'QualifiedDublinCoreElementHistory'
        db.delete_table('DublinCore_qualifieddublincoreelementhistory')


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
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['DublinCore']
