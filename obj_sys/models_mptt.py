from models_ufs_obj import *


try:
    # noinspection PyUnresolvedReferences
    from mptt.models import MPTTModel, TreeForeignKey

    class UfsObjInTree(MPTTModel):
        ufs_obj = models.ForeignKey(UfsObj, null=True, blank=True)
        parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
        user = models.ForeignKey(User, null=True, blank=True)

        def __unicode__(self):
            try:
                return unicode(self.ufs_obj.ufs_url + '---------> uuid:' + self.ufs_obj.uuid)
            except:
                return "ufs obj is null"

except ImportError:
    pass