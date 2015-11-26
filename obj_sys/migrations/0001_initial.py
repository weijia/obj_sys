# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Description'
        db.create_table('obj_sys_description', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('obj_sys', ['Description'])

        # Adding model 'UfsObj'
        db.create_table('obj_sys_ufsobj', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('full_path', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('ufs_url', self.gf('django.db.models.fields.TextField')()),
            ('uuid', self.gf('django.db.models.fields.CharField')(default='21516101-59a0-4741-9c2a-31e96423fb89', unique=True, max_length=60)),
            ('head_md5', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('total_md5', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('last_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('obj_created', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('obj_last_modified', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('size', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('description_json', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('valid', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('ufs_obj_type', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal('obj_sys', ['UfsObj'])

        # Adding M2M table for field relations on 'UfsObj'
        m2m_table_name = db.shorten_name('obj_sys_ufsobj_relations')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_ufsobj', models.ForeignKey(orm['obj_sys.ufsobj'], null=False)),
            ('to_ufsobj', models.ForeignKey(orm['obj_sys.ufsobj'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_ufsobj_id', 'to_ufsobj_id'])

        # Adding M2M table for field descriptions on 'UfsObj'
        m2m_table_name = db.shorten_name('obj_sys_ufsobj_descriptions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ufsobj', models.ForeignKey(orm['obj_sys.ufsobj'], null=False)),
            ('description', models.ForeignKey(orm['obj_sys.description'], null=False))
        ))
        db.create_unique(m2m_table_name, ['ufsobj_id', 'description_id'])

        # Adding model 'UfsObjInTree'
        db.create_table('obj_sys_ufsobjintree', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ufs_obj', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['obj_sys.UfsObj'], null=True, blank=True)),
            ('parent', self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['obj_sys.UfsObjInTree'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            (u'lft', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'rght', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'tree_id', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
            (u'level', self.gf('django.db.models.fields.PositiveIntegerField')(db_index=True)),
        ))
        db.send_create_signal('obj_sys', ['UfsObjInTree'])


    def backwards(self, orm):
        # Deleting model 'Description'
        db.delete_table('obj_sys_description')

        # Deleting model 'UfsObj'
        db.delete_table('obj_sys_ufsobj')

        # Removing M2M table for field relations on 'UfsObj'
        db.delete_table(db.shorten_name('obj_sys_ufsobj_relations'))

        # Removing M2M table for field descriptions on 'UfsObj'
        db.delete_table(db.shorten_name('obj_sys_ufsobj_descriptions'))

        # Deleting model 'UfsObjInTree'
        db.delete_table('obj_sys_ufsobjintree')


    models = {
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
        'obj_sys.description': {
            'Meta': {'object_name': 'Description'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'obj_sys.ufsobj': {
            'Meta': {'object_name': 'UfsObj'},
            'description_json': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'descriptions': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'descriptions'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['obj_sys.Description']"}),
            'full_path': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'head_md5': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'obj_created': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'obj_last_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'relations': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'relations_rel_+'", 'null': 'True', 'to': "orm['obj_sys.UfsObj']"}),
            'size': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'total_md5': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'ufs_obj_type': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'ufs_url': ('django.db.models.fields.TextField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'a0096aff-9812-4616-9cdf-e9f8d0edca4f'", 'unique': 'True', 'max_length': '60'}),
            'valid': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'obj_sys.ufsobjintree': {
            'Meta': {'object_name': 'UfsObjInTree'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['obj_sys.UfsObjInTree']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'ufs_obj': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['obj_sys.UfsObj']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['obj_sys']