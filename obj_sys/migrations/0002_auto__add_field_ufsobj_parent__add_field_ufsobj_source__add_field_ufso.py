# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'UfsObj.parent'
        db.add_column('obj_sys_ufsobj', 'parent',
                      self.gf('mptt.fields.TreeForeignKey')(blank=True, related_name='children', null=True, to=orm['obj_sys.UfsObj']),
                      keep_default=False)

        # Adding field 'UfsObj.source'
        db.add_column('obj_sys_ufsobj', 'source',
                      self.gf('django.db.models.fields.IntegerField')(default=1, null=True, blank=True),
                      keep_default=False)

        # Adding field 'UfsObj.source_ip'
        db.add_column('obj_sys_ufsobj', 'source_ip',
                      self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True),
                      keep_default=False)

        # Adding field 'UfsObj.position'
        db.add_column('obj_sys_ufsobj', 'position',
                      self.gf('geoposition.fields.GeopositionField')(default=None, max_length=42, null=True, blank=True),
                      keep_default=False)

        # Adding field 'UfsObj.lft'
        db.add_column('obj_sys_ufsobj', u'lft',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True),
                      keep_default=False)

        # Adding field 'UfsObj.rght'
        db.add_column('obj_sys_ufsobj', u'rght',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True),
                      keep_default=False)

        # Adding field 'UfsObj.tree_id'
        db.add_column('obj_sys_ufsobj', u'tree_id',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True),
                      keep_default=False)

        # Adding field 'UfsObj.level'
        db.add_column('obj_sys_ufsobj', u'level',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1, db_index=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'UfsObj.parent'
        db.delete_column('obj_sys_ufsobj', 'parent_id')

        # Deleting field 'UfsObj.source'
        db.delete_column('obj_sys_ufsobj', 'source')

        # Deleting field 'UfsObj.source_ip'
        db.delete_column('obj_sys_ufsobj', 'source_ip')

        # Deleting field 'UfsObj.position'
        db.delete_column('obj_sys_ufsobj', 'position')

        # Deleting field 'UfsObj.lft'
        db.delete_column('obj_sys_ufsobj', u'lft')

        # Deleting field 'UfsObj.rght'
        db.delete_column('obj_sys_ufsobj', u'rght')

        # Deleting field 'UfsObj.tree_id'
        db.delete_column('obj_sys_ufsobj', u'tree_id')

        # Deleting field 'UfsObj.level'
        db.delete_column('obj_sys_ufsobj', u'level')


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
            u'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            u'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'obj_created': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'obj_last_modified': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['obj_sys.UfsObj']"}),
            'position': ('geoposition.fields.GeopositionField', [], {'default': 'None', 'max_length': '42', 'null': 'True', 'blank': 'True'}),
            'relations': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'relations_rel_+'", 'null': 'True', 'to': "orm['obj_sys.UfsObj']"}),
            u'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'size': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'source': ('django.db.models.fields.IntegerField', [], {'default': '1', 'null': 'True', 'blank': 'True'}),
            'source_ip': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'total_md5': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            u'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'ufs_obj_type': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'ufs_url': ('django.db.models.fields.TextField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'default': "'88490d8b-e119-43fd-94ef-17e16b33f771'", 'unique': 'True', 'max_length': '60'}),
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