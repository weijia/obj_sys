from ufs_obj_models import *


try:
    # noinspection PyUnresolvedReferences
    from mptt.models import MPTTModel, TreeForeignKey

    class UfsObjInTree(MPTTModel):
        ufs_obj = models.ForeignKey(UfsObj, null=True, blank=True)
        parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
        user = models.ForeignKey(User, null=True, blank=True)

        def __unicode__(self):
            return unicode(self.ufs_obj.ufs_url + '---------> uuid:' + self.ufs_obj.uuid)

except ImportError:
    pass