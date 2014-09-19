from django.contrib import admin

from objsys.models import UfsObj
from objsys.models import Description
#admin.site.register(UfsObj)
#admin.site.register(Description)
from djangoautoconf.auto_conf_admin_utils import register_all


register_all([UfsObj, Description])


