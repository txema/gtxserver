# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HistoricalStatus'
        db.create_table(u'gtxapi_historicalstatus', (
            (u'id', self.gf('django.db.models.fields.IntegerField')(db_index=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=100)),
            (u'history_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            (u'history_date', self.gf('django.db.models.fields.DateTimeField')()),
            (u'history_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            (u'history_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'gtxapi', ['HistoricalStatus'])

        # Adding model 'Status'
        db.create_table('status', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'gtxapi', ['Status'])

        # Adding model 'HistoricalTag'
        db.create_table(u'gtxapi_historicaltag', (
            (u'id', self.gf('django.db.models.fields.IntegerField')(db_index=True, blank=True)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=100)),
            (u'history_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            (u'history_date', self.gf('django.db.models.fields.DateTimeField')()),
            (u'history_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            (u'history_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'gtxapi', ['HistoricalTag'])

        # Adding model 'Tag'
        db.create_table('tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'gtxapi', ['Tag'])

        # Adding model 'HistoricalTask'
        db.create_table(u'gtxapi_historicaltask', (
            (u'id', self.gf('django.db.models.fields.IntegerField')(db_index=True, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('owner_id', self.gf('django.db.models.fields.IntegerField')(db_index=True, null=True, blank=True)),
            ('created_by_id', self.gf('django.db.models.fields.IntegerField')(db_index=True, null=True, blank=True)),
            (u'history_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            (u'history_date', self.gf('django.db.models.fields.DateTimeField')()),
            (u'history_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            (u'history_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal(u'gtxapi', ['HistoricalTask'])

        # Adding model 'Task'
        db.create_table('tasks', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tasks_assigned', to=orm['auth.User'])),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='tasks_created', to=orm['auth.User'])),
        ))
        db.send_create_signal(u'gtxapi', ['Task'])

        # Adding M2M table for field statuses on 'Task'
        m2m_table_name = db.shorten_name('tasks_statuses')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('task', models.ForeignKey(orm[u'gtxapi.task'], null=False)),
            ('status', models.ForeignKey(orm[u'gtxapi.status'], null=False))
        ))
        db.create_unique(m2m_table_name, ['task_id', 'status_id'])

        # Adding M2M table for field tags on 'Task'
        m2m_table_name = db.shorten_name('tasks_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('task', models.ForeignKey(orm[u'gtxapi.task'], null=False)),
            ('tag', models.ForeignKey(orm[u'gtxapi.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['task_id', 'tag_id'])


    def backwards(self, orm):
        # Deleting model 'HistoricalStatus'
        db.delete_table(u'gtxapi_historicalstatus')

        # Deleting model 'Status'
        db.delete_table('status')

        # Deleting model 'HistoricalTag'
        db.delete_table(u'gtxapi_historicaltag')

        # Deleting model 'Tag'
        db.delete_table('tag')

        # Deleting model 'HistoricalTask'
        db.delete_table(u'gtxapi_historicaltask')

        # Deleting model 'Task'
        db.delete_table('tasks')

        # Removing M2M table for field statuses on 'Task'
        db.delete_table(db.shorten_name('tasks_statuses'))

        # Removing M2M table for field tags on 'Task'
        db.delete_table(db.shorten_name('tasks_tags'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'gtxapi.historicalstatus': {
            'Meta': {'ordering': "(u'-history_date', u'-history_id')", 'object_name': 'HistoricalStatus'},
            u'history_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'history_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'history_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'history_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            u'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'gtxapi.historicaltag': {
            'Meta': {'ordering': "(u'-history_date', u'-history_id')", 'object_name': 'HistoricalTag'},
            u'history_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'history_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'history_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'history_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            u'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'gtxapi.historicaltask': {
            'Meta': {'ordering': "(u'-history_date', u'-history_id')", 'object_name': 'HistoricalTask'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'created_by_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'history_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'history_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'history_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'history_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            u'id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'blank': 'True'}),
            'owner_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'})
        },
        u'gtxapi.status': {
            'Meta': {'object_name': 'Status', 'db_table': "'status'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'gtxapi.tag': {
            'Meta': {'object_name': 'Tag', 'db_table': "'tag'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'gtxapi.task': {
            'Meta': {'ordering': "['created_at']", 'object_name': 'Task', 'db_table': "'tasks'"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tasks_created'", 'to': u"orm['auth.User']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'tasks_assigned'", 'to': u"orm['auth.User']"}),
            'statuses': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['gtxapi.Status']", 'symmetrical': 'False'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['gtxapi.Tag']", 'null': 'True', 'symmetrical': 'False'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['gtxapi']