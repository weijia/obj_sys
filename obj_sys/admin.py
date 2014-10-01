from djangoautoconf.auto_conf_admin_utils import register_all_in_module
import models
from mptt_models import UfsObjInTree
from django.contrib import admin
from mptt.admin import MPTTModelAdmin


register_all_in_module(models)
admin.site.register(UfsObjInTree, MPTTModelAdmin)