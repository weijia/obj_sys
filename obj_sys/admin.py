from django_mptt_admin.admin import DjangoMpttAdmin

from djangoautoconf.auto_conf_admin_tools.admin_register import AdminRegister
# from djangoautoconf.auto_conf_admin_utils import register_all_in_module
import models
from djangoautoconf.auto_conf_admin_tools.filter_horizontal_feature import FilterHorizontalFeature
from djangoautoconf.auto_conf_admin_tools.foreign_key_auto_complete import ForeignKeyAutoCompleteFeature
from djangoautoconf.auto_conf_admin_tools.guardian_feature import GuardianFeature
from djangoautoconf.auto_conf_admin_tools.import_export_feature import ImportExportFeature
from djangoautoconf.auto_conf_admin_tools.reversion_feature import ReversionFeature
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
from obj_sys.models_ufs_obj import UfsObj, Description


# class DjangoMpttAdminReg(AdminRegister):
#     # default_feature_list = [ImportExportFeature, GuardianFeature]
#     default_feature_list = []
# r = DjangoMpttAdminReg()

r = AdminRegister()
f = ForeignKeyAutoCompleteFeature()
h = FilterHorizontalFeature(('descriptions', 'relations'))
f.set_search_field_by_model({UfsObj: ("uuid", "ufs_url", "full_path")})
r.add_feature(f)
r.add_feature(h)
r.add_feature(ReversionFeature())
r.register(UfsObj)
# r.add_feature(FilterHorizontalFeature(("relations", "descriptions")))
# r.register(UfsObj, [DjangoMpttAdmin])

# from django.contrib import admin
# from django_mptt_admin.admin import DjangoMpttAdmin
#
#
# class UfsObjAdmin(DjangoMpttAdmin):
#     pass
#
#
# admin.site.register(UfsObj, UfsObjAdmin)


r = AdminRegister()
r.add_feature(ReversionFeature())
r.register_all_models(models)