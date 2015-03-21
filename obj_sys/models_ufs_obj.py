from django.db import models
from django.contrib.auth.models import User
from django.utils.datetime_safe import datetime
from djangoautoconf.django_utils import get_new_uuid
import datetime


class Description(models.Model):
    content = models.TextField(null=True, blank=True, help_text="Content for the description")

    def __unicode__(self):
        return unicode(self.content)

    # class Meta:
    #     db_table = 'objsys_description'


class UfsObj(models.Model):
    UFS_OBJ_TYPE_CHOICES = (
        (1, 'UFS OBJ TYPE (file or URL)'),
        (2, 'STORAGE_ITEM'),
        (3, 'TBD')
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
            self.obj_created = datetime.datetime.today()
        self.obj_last_modified = datetime.datetime.today()
        super(UfsObj, self).save(*args, **kwargs)  # Call the "real" save() method.

    def get_type(self):
        if not (self.full_path is None):
            try:
                from objsys_local.views import get_type_from_full_path
                return get_type_from_full_path(self)
            except ImportError:
                pass
        return 'unknown'

    # class Meta:
    #     db_table = 'objsys_ufsobj'