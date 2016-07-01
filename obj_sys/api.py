from django.utils.timezone import is_naive
from tastypie import fields
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie.resources import ModelResource
from tastypie.authorization import DjangoAuthorization
from tastypie.serializers import Serializer
from djangoautoconf.django_utils import retrieve_param
from djangoautoconf.req_with_auth import DjangoUserAuthentication, verify_access_token
from models import UfsObj
# from django.contrib.auth.models import User, Group
from tagging.models import Tag
from tagging.models import TaggedItem
from models import Description


# Ref: http://www.tryolabs.com/Blog/2013/03/16/displaying-timezone-aware-dates-tastypie/
class DateSerializerWithTimezone(Serializer):
    """
    Our own serializer to format datetimes in ISO 8601 but with timezone
    offset.
    """

    def format_datetime(self, data):
        # If naive or rfc-2822, default behavior...
        if is_naive(data) or self.datetime_formatting == 'rfc-2822':
            return super(DateSerializerWithTimezone, self).format_datetime(data)
        return data.isoformat()


class DescriptionResource(ModelResource):
    class Meta:
        queryset = Description.objects.all()
        resource_name = 'description'
        # authentication = SessionAuthentication()
        authentication = DjangoUserAuthentication()
        authorization = DjangoAuthorization()
        filtering = {
            "content": ALL,
        }


'''
class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
'''


# noinspection PyMethodMayBeStatic
class UfsObjResource(ModelResource):
    # json_indent = 2
    descriptions = fields.ToManyField(DescriptionResource, 'descriptions', full=True)
    parent = fields.ForeignKey('self', 'parent', null=True)

    def get_object_list(self, request):
        # return super(UfsObjResource, self).get_object_list(request).filter(start_date__gte=now)
        data = retrieve_param(request)

        ufs_objects = self.get_initial_queryset(data, request)

        if not ("all" in data):
            ufs_objects = ufs_objects.filter(valid=True)

        if "type" in data:
            ufs_objects = ufs_objects.filter(ufs_obj_type=int(data["type"]))

        if "consumer_key" in data:
            ufs_objects = ufs_objects.filter(user=verify_access_token(data["consumer_key"]).user)

        if "parent_url" in data:
            if data["parent_url"] == "bar://root":
                ufs_objects = ufs_objects.filter(parent=None)
            else:
                ufs_objects = ufs_objects.filter(parent__ufs_url=data["parent_url"])

        return ufs_objects

    def get_initial_queryset(self, data, request):
        tag_str = self.get_tag_str_for_whole_session(data, request)
        if tag_str is None:
            ufs_objects = super(UfsObjResource, self).get_object_list(request)
        else:
            request.session["tag"] = tag_str
            ufs_objects = self.__get_ufs_objects_with_tags(tag_str)
        return ufs_objects

    def get_tag_str_for_whole_session(self, data, request):
        if self.__is_new_tag_query(request, data):
            tag_str = data.get("tag", None)
        else:
            tag_str = request.session.get("tag", None)
        return tag_str

    def dehydrate(self, bundle):
        res = []
        for tag in bundle.obj.tags:
            res.append(tag)
        bundle.data["tags"] = res
        user = bundle.obj.user
        if not (user is None):
            bundle.data["username"] = user.username
        # bundle.data["parent"] = bundle.obj.parent.ufs_url
        return bundle

    '''
    def build_filters(self, filters=None):
        if filters is None:
            filters = {}

        orm_filters = super(MyResource, self).build_filters(filters)

        if "tag" in filters:
            sqs = SearchQuerySet().auto_query(filters['q'])

            orm_filters["pk__in"] = [i.pk for i in sqs]

        return orm_filters
    '''

    class Meta:
        # When listing all ufs objects, sort timestamp ascend, it means oldest first
        queryset = UfsObj.objects.all().order_by("timestamp").select_related('parent')
        resource_name = 'ufsobj'
        always_return_data = True
        # authentication = SessionAuthentication()
        authentication = DjangoUserAuthentication()
        authorization = DjangoAuthorization()
        filtering = {
            "ufs_url": ('contains', 'exact'),
            "full_path": ('contains', 'iendswith'),
            "descriptions": ALL_WITH_RELATIONS,
            # "parent": ALL_WITH_RELATIONS,
            "ufs_obj_type": ALL,
        }
        serializer = DateSerializerWithTimezone()

    def __get_ufs_objects_with_tags(self, tag):
        try:
            obj_tag = Tag.objects.get(name=tag)
            # When enumerating tagged items use descent timestamp, it means newest first
            ufs_objects = TaggedItem.objects.get_by_model(UfsObj, obj_tag).order_by('-timestamp').filter(
                valid=True)
        except:
            ufs_objects = UfsObj.objects.none()
        return ufs_objects

    def __is_new_tag_query(self, request, data):
        """
        There is a tag value in session and there is also a offset value in request, so it is a request to continue
        the last tag query.
        """
        if ("tag" in request.session) and \
                ("offset" in data):  # Do not have offset means it may be a new serial of object query
            return True
        return False

'''
class TagResource(ModelResource):
    class Meta:
        queryset = Tag.objects.usage_for_model(UfsObj)
        resource_name = 'tag'
        #authentication = SessionAuthentication()
        authentication = DjangoUserAuthentication()
        authorization = DjangoAuthorization()
'''

'''
class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        #authentication = SessionAuthentication()
        authentication = DjangoUserAuthentication()
        authorization = DjangoAuthorization()
        excludes = ['email', 'password', 'is_staff', 'is_superuser']
        filtering = {
            "username": ('exact', 'startswith',),
        }
        
class GroupResource(ModelResource):
    class Meta:
        queryset = Group.objects.all()
        resource_name = 'group'
        #authentication = SessionAuthentication()
        authentication = DjangoUserAuthentication()
        authorization = DjangoAuthorization()
'''
