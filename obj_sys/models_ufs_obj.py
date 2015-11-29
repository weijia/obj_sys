from django.db import models
from django.contrib.auth.models import User
from django.utils.datetime_safe import datetime
from pytz import utc
from mptt.models import MPTTModel, TreeForeignKey
from geoposition.fields import GeopositionField
from djangoautoconf.django_utils import get_new_uuid


class Description(models.Model):
    content = models.TextField(null=True, blank=True, help_text="Content for the description")

    def __unicode__(self):
        return unicode(self.content)

        # class Meta:
        #     db_table = 'objsys_description'


class UfsObj(MPTTModel):
    INDEXING_FILE = 1004
    UFS_OBJ_TYPE = 1
    UFS_OBJ_TYPE_CHOICES = (
        (UFS_OBJ_TYPE, 'UFS OBJ TYPE (file or URL)'),
        (2, 'STORAGE_ITEM'),
        (3, 'CLIPBOARD'),
        (4, 'INDEXED_FILE'),
        (1000, 'TBD'),
        (INDEXING_FILE, 'INDEXING_FILE'),
    )
    UFS_SOURCE_CHOICES = (
        (1, 'WEB_POST'),
        (2, 'STORAGE_MANAGER'),
        (3, 'CLIPBOARD'),
        (4, 'TBD'),
    )
    full_path = models.TextField(null=True, blank=True)
    ufs_url = models.TextField(help_text='start with ufs:// or uuid:// etc.')
    uuid = models.CharField(max_length=60, default=get_new_uuid, unique=True,
                            help_text='the uuid string of the object, no "uuid" prefix needed')
    head_md5 = models.CharField(max_length=60, null=True, blank=True,
                                help_text="the md5 for the header of the object")
    total_md5 = models.CharField(max_length=60, null=True, blank=True,
                                 help_text="the entire object's md5 hash value")
    timestamp = models.DateTimeField('date this object record is published to database', auto_now_add=True)
    last_modified = models.DateTimeField('the last modified date for the object record in database', auto_now=True)

    obj_created = models.DateTimeField('the created date for the object itself', null=True, blank=True)
    obj_last_modified = models.DateTimeField('the last modified date for the object itself', null=True, blank=True)

    size = models.BigIntegerField(null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True)
    description_json = models.TextField(null=True, blank=True, help_text="JSON description for this object")
    valid = models.BooleanField(default=True, help_text="is this field valid")
    relations = models.ManyToManyField("self", related_name='related_objs', null=True, blank=True,
                                       help_text="Related other information objects")
    descriptions = models.ManyToManyField(Description, related_name='descriptions', null=True, blank=True,
                                          help_text="Descriptions for this object")
    ufs_obj_type = models.IntegerField(choices=UFS_OBJ_TYPE_CHOICES, default=1)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    source = models.IntegerField(choices=UFS_SOURCE_CHOICES, default=1, null=True, blank=True)
    source_ip = models.CharField(max_length=60, null=True, blank=True,
                                 help_text="IP address from which the object was posted")
    position = GeopositionField(default=None, null=True, blank=True)
    added_from_app = models.CharField(max_length=30, null=True, blank=True,
                                      help_text="the app name who added this entry")

    def get_one_description(self):
        try:
            return self.descriptions.all().order_by("-pk")[0].content
        except IndexError:
            return ""

    def __unicode__(self):
        return unicode(self.ufs_url + " - " + self.get_one_description() + '---------> uuid:' + self.uuid)

    def save(self, *args, **kwargs):
        if not (self.full_path is None):
            try:
                from objsys_local.views import set_fields_from_full_path

                set_fields_from_full_path(self)
            except:
                pass
        if not self.id:
            self.obj_created = datetime.utcnow().replace(tzinfo=utc)
        self.obj_last_modified = datetime.utcnow().replace(tzinfo=utc)
        super(UfsObj, self).save(*args, **kwargs)  # Call the "real" save() method.

    def get_type(self):
        if not (self.full_path is None):
            try:
                from objsys_local.views import get_type_from_full_path

                return get_type_from_full_path(self)
            except ImportError:
                pass
        return 'unknown'
