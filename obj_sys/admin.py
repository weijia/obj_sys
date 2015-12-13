from djangoautoconf.auto_conf_admin_tools.admin_register import AdminRegister
# from djangoautoconf.auto_conf_admin_utils import register_all_in_module
import models
from djangoautoconf.auto_conf_admin_tools.foreign_key_auto_complete import ForeignKeyAutoCompleteFeature
from models_mptt import UfsObjInTree
from django.contrib import admin
from mptt.admin import MPTTModelAdmin
# from django.conf import settings
#
# """
# if "guardian" in settings.INSTALLED_APPS:
#     from guardian.admin import GuardedModelAdmin as SingleModelAdmin
# else:
#     from django.contrib.admin import ModelAdmin as SingleModelAdmin
# """
#
#
# class UfsObjAdmin(object):
#     def queryset(self, request):
#         qs = super(UfsObjAdmin, self).queryset(request)
#
#         # If super-user, show all comments
#         if request.user.is_superuser:
#             return qs
#
#         return qs.filter(user=request.user)
#
#
# register_all_in_module(models_obj_rel, admin_class_list=[UfsObjAdmin])


# from reversion.helpers import patch_admin
#
# patch_admin(models_obj_rel.UfsObj)
from obj_sys.models_ufs_obj import UfsObj

admin.site.register(UfsObjInTree, MPTTModelAdmin)
# admin.site.register(UfsObj, MPTTModelAdmin)

r = AdminRegister()
f = ForeignKeyAutoCompleteFeature()
f.set_search_field_by_model({UfsObj: ("uuid", "ufs_url", "full_path")})
r.add_feature(f)
r.register_all_models(models)