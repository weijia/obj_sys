from api import UfsObjResource, DescriptionResource
from models import UfsObj
from tastypie.authorization import DjangoAuthorization
from djangoautoconf.django_utils import retrieve_param
from djangoautoconf.req_with_auth import DjangoUserAuthentication
from tastypie.constants import ALL_WITH_RELATIONS
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
    # json_indent = 2
    # descriptions = fields.ToOneField(DescriptionResource, 'descriptions')
    descriptions = fields.ToManyField(DescriptionResource, 'descriptions', full=True)

    class Meta:
        queryset = UfsObj.objects.all()
        resource_name = 'ufs_obj_in_tree'
        # authentication = SessionAuthentication()
        authentication = DjangoUserAuthentication()
        authorization = DjangoAuthorization()

        filtering = {
            "ufs_obj": ALL_WITH_RELATIONS,
        }

    def get_object_list(self, request):
        data = retrieve_param(request)
        if "parent_url" in data:
            if data["parent_url"] == "bar://root":
                parent_obj_in_tree = None
            else:
                query_req = {"valid": True, "ufs_obj_type": 2, "ufs_url": data["parent_url"],
                             "user": request.user}
                parent_obj = UfsObj.objects.filter(**query_req)
            return UfsObj.objects.filter(parent=parent_obj, user=request.user,
                                         valid=True)
        return super(UfsObjInTreeResource, self).get_object_list(request)

    def dehydrate(self, bundle):
        if not (bundle.obj.parent is None):
            bundle.data["parent"] = bundle.obj.parent.ufs_obj.ufs_url
        return bundle
