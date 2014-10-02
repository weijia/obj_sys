from djangoautoconf.auto_conf_admin_utils import register_all_in_module
import models_obj_rel
from models_mptt import UfsObjInTree
from django.contrib import admin
from mptt.admin import MPTTModelAdmin


register_all_in_module(models_obj_rel)
admin.site.register(UfsObjInTree, MPTTModelAdmin)