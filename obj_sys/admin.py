from ajax_select import make_ajax_form
from django.contrib.admin import AdminSite
from ufs_tools.string_tools import class_name_to_low_case

from djangoautoconf.auto_conf_admin_tools.admin_attr_feature import AdminAttrFeature
from djangoautoconf.auto_conf_admin_tools.admin_features.admin_tagging_feature import AdminTaggingFeature
from djangoautoconf.auto_conf_admin_tools.admin_register import AdminRegister
import models
# from djangoautoconf.auto_conf_admin_tools.filter_horizontal_feature import FilterHorizontalFeature
# from djangoautoconf.auto_conf_admin_tools.foreign_key_auto_complete import ForeignKeyAutoCompleteFeature
from djangoautoconf.auto_conf_admin_tools.reversion_feature import ReversionFeature
# from normal_admin.user_admin import UserAdminAuthenticationForm, get_admin_site
from obj_sys.models_ufs_obj import UfsObj


r = AdminRegister()
# f = ForeignKeyAutoCompleteFeature()
# # h = FilterHorizontalFeature(('descriptions', 'relations'))
# f.set_search_field_by_model({UfsObj: ("uuid", "ufs_url", "full_path")})
# r.add_feature(f)
# r.add_feature(h)
# h = AdminAttrFeature({"filter_horizontal": ("descriptions", )})
# raw = AdminAttrFeature({"raw_id_fields": ("relations",)})
# r.add_feature(raw)
# r.add_feature(h)
a = AdminAttrFeature({"form": make_ajax_form(UfsObj, {"relations": "ufs_obj",
                                                      "parent": "ufs_obj",
                                                      "descriptions": "description"}),
                      "list_filter": ('source', 'ufs_obj_type')
                      })

r.add_feature(a)
r.add_feature(ReversionFeature())
r.add_feature(AdminTaggingFeature())
r.register(UfsObj)


r = AdminRegister()
r.add_feature(ReversionFeature())
r.register_all_models(models)


# obj_sys_admin_site = get_admin_site("ObjSysAdminSite")
#
# r = AdminRegister(admin_site_list=[obj_sys_admin_site], feature_list=[])
# a = AdminAttrFeature({"form": make_ajax_form(UfsObj, {"relations": "ufs_obj",
#                                                       "parent": "ufs_obj",
#                                                       "descriptions": "description"}),
#                       "list_filter": ('source', 'ufs_obj_type')
#                       })
#
# r.add_feature(a)
# r.add_feature(ReversionFeature())
# r.add_feature(AdminTaggingFeature())
# r.register(UfsObj)
