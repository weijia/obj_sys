# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mptt.fields
import geoposition.fields
import djangoautoconf.django_utils
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(help_text=b'Content for the description', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ObjRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('relation', models.CharField(help_text=b'relation text', max_length=60, null=True, blank=True)),
                ('valid', models.BooleanField(default=True, help_text=b'is this field valid')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name=b'date this object is published to database')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name=b'the last modified date for the object in database')),
            ],
        ),
        migrations.CreateModel(
            name='UfsObj',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_path', models.TextField(null=True, blank=True)),
                ('ufs_url', models.TextField(help_text=b'start with ufs:// or uuid:// etc.')),
                ('uuid', models.CharField(default=djangoautoconf.django_utils.get_new_uuid, help_text=b'the uuid string of the object, no "uuid" prefix needed', unique=True, max_length=60)),
                ('head_md5', models.CharField(help_text=b'the md5 for the header of the object', max_length=60, null=True, blank=True)),
                ('total_md5', models.CharField(help_text=b"the entire object's md5 hash value", max_length=60, null=True, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name=b'date this object record is published to database')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name=b'the last modified date for the object record in database')),
                ('obj_created', models.DateTimeField(null=True, verbose_name=b'the created date for the object itself', blank=True)),
                ('obj_last_modified', models.DateTimeField(null=True, verbose_name=b'the last modified date for the object itself', blank=True)),
                ('size', models.BigIntegerField(null=True, blank=True)),
                ('description_json', models.TextField(help_text=b'JSON description for this object', null=True, blank=True)),
                ('valid', models.BooleanField(default=True, help_text=b'is this field valid')),
                ('ufs_obj_type', models.IntegerField(default=1, choices=[(1, b'UFS OBJ TYPE (file or URL)'), (2, b'STORAGE_ITEM'), (3, b'CLIPBOARD'), (1000, b'CUSTOMIZABLE_START')])),
                ('source', models.IntegerField(default=1, null=True, blank=True, choices=[(1, b'WEB_POST'), (2, b'STORAGE_MANAGER'), (3, b'CLIPBOARD'), (1000, b'CUSTOMIZABLE_START'), (1004, b'INDEXER'), (4, b'SOURCE_CLIPBOARD_FROM_EVERNOTE')])),
                ('source_ip', models.CharField(help_text=b'IP address from which the object was posted', max_length=60, null=True, blank=True)),
                ('position', geoposition.fields.GeopositionField(default=None, max_length=42, null=True, blank=True)),
                ('added_from_app', models.CharField(help_text=b'the app name who added this entry', max_length=30, null=True, blank=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('descriptions', models.ManyToManyField(help_text=b'Descriptions for this object', related_name='descriptions', to='obj_sys.Description', blank=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', blank=True, to='obj_sys.UfsObj', null=True)),
                ('relations', models.ManyToManyField(help_text=b'Related other information objects', related_name='_ufsobj_relations_+', to='obj_sys.UfsObj', blank=True)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='objrelation',
            name='from_obj',
            field=models.ForeignKey(related_name='from_obj', blank=True, to='obj_sys.UfsObj', null=True),
        ),
        migrations.AddField(
            model_name='objrelation',
            name='to_obj',
            field=models.ForeignKey(related_name='to_obj', blank=True, to='obj_sys.UfsObj', null=True),
        ),
    ]
