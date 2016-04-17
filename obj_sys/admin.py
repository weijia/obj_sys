from ajax_select import make_ajax_form
from djangoautoconf.auto_conf_admin_tools.admin_attr_feature import AdminAttrFeature
from djangoautoconf.auto_conf_admin_tools.admin_register import AdminRegister
import models
# from djangoautoconf.auto_conf_admin_tools.filter_horizontal_feature import FilterHorizontalFeature
# from djangoautoconf.auto_conf_admin_tools.foreign_key_auto_complete import ForeignKeyAutoCompleteFeature
from djangoautoconf.auto_conf_admin_tools.reversion_feature import ReversionFeature
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
                                                      "descriptions": "description"})})

r.add_feature(a)
r.add_feature(ReversionFeature())
r.register(UfsObj)


r = AdminRegister()
r.add_feature(ReversionFeature())
r.register_all_models(models)