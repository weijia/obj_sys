from api import UfsObjResource
from models import UfsObj
from tastypie.authorization import DjangoAuthorization
from djangoautoconf.django_utils import retrieve_param
from djangoautoconf.req_with_auth import DjangoUserAuthentication
from models_mptt import UfsObjInTree
from tastypie.resources import ModelResource
from tastypie import fields


def get_user_valid_item_queryset(user):
    return UfsObj.objects.filter(user=user, valid=True)


class FilterCollection(object):
    def filter_as_requested(req):
        object_queryset = UfsObj.objects.all()
        for attr in UfsObj._meta.get_all_field_names:
            object_queryset


class UfsObjInTreeResource(ModelResource):
    ufs_obj = fields.ForeignKey(UfsObjResource, 'ufs_obj', full=True)

    class Meta:
        queryset = UfsObjInTree.objects.all()
        resource_name = 'ufs_obj_in_tree'
        #authentication = SessionAuthentication()
        authentication = DjangoUserAuthentication()
        authorization = DjangoAuthorization()

    def get_object_list(self, request):
        data = retrieve_param(request)
        if "parent_url" in data:
            if data["parent_url"] == "bar://root":
                parent_obj_in_tree = None
            else:
                query_req = {"valid": True, "ufs_obj_type": 2, "ufs_url": data["parent_url"], "user": request.user}
                parent_obj = UfsObj.objects.filter(**query_req)
                parent_obj_in_tree = UfsObjInTree.objects.filter(ufs_obj=parent_obj)[0]
            return UfsObjInTree.objects.filter(parent=parent_obj_in_tree)
        return super(UfsObjInTreeResource, self).get_object_list(request)