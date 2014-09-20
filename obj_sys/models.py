# Create your models here.
from ufs_obj_models import *


class ObjRelation(models.Model):
    from_obj = models.ForeignKey(UfsObj, null=True, blank=True, related_name="from")
    to_obj = models.ForeignKey(UfsObj, null=True, blank=True, related_name="to")
    relation = models.CharField(max_length=60, null=True, blank=True,
                                help_text="relation text")
    valid = models.BooleanField(default=True, help_text="is this field valid")
    timestamp = models.DateTimeField('date this object is published to database', auto_now_add=True)
    last_modified = models.DateTimeField('the last modified date for the object in database', auto_now=True)


try:
    import tagging
    tagging.register(UfsObj)
except:
    pass


try:
    from mptt.models import MPTTModel, TreeForeignKey

    class UfsObjInTree(MPTTModel):
        ufs_obj = models.ForeignKey(UfsObj, null=True, blank=True)
        parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

except ImportError:
    pass
