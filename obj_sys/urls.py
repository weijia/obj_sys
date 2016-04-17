from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from djangoautoconf.ajax_select_utils.ajax_select_channel_generator import register_channel
from djangoautoconf.django_rest_framework_utils.serializer_generator import get_detail_api_class
# from towel.modelview import ModelView
from models import UfsObj, Description
from tagging.models import Tag
from api import UfsObjResource
from add_tag_template_view import AddTagTemplateView
from add_tag_template_view_local import AddTagTemplateViewLocal
from api_ufs_obj_in_tree import UfsObjInTreeResource
from ufs_obj_in_tree_view import ItemTreeView
from rss import LatestEntriesFeed


ufs_obj_resource = UfsObjResource()
ufs_obj_in_tree_resource = UfsObjInTreeResource()
# tag_resource = TagResource()

# obj_views = ModelView(UfsObj)

# resource_views_ajax = ModelView(BookableResource, base_template="modal.html")
# resource_booking_req_views_ajax = ModelView(BookingRequest, base_template="modal.html")

################################
# The folloing codes can not be put in admin, otherwise there will be template error:
# Reverse for 'obj_sys_description_add' with arguments '()' and keyword arguments '{}' not found. 0 pattern(s) tried: []
# Don't know why
register_channel(UfsObj, ["ufs_url", "full_path", "descriptions__content"])
register_channel(Description, ["content", ])


urlpatterns = patterns('',
                       # place it at whatever base url you like
                       # url(r'^ajax_select/', include(ajax_select_urls)),
                       url(r'^tagging/$', login_required(AddTagTemplateView.as_view())),
                       url(r'^$', login_required(
                           ItemTreeView.as_view(item_class=UfsObj,
                                                # default_level=2,
                                                ufs_obj_type=UfsObj.TYPE_UFS_OBJ,
                                                template_name='obj_sys/mptt_item_tree.html'))),
                       url(r'^tagging_local/$', login_required(AddTagTemplateViewLocal.as_view())),
                       url(r'^tagging/(?P<news_item_pk>\d+)/$', login_required(AddTagTemplateView.as_view()),
                           name="news-item"),
                       url(r'^manager/$', 'obj_sys.views.manager'),
                       url(r'^listing/$', 'obj_sys.views.listing'),
                       url(r'^homepage/$', 'obj_sys.views.listing_with_description'),
                       (r'^latest/feed/$', LatestEntriesFeed()),
                       # url(r'^qrcode/$', 'thumbapp.views.gen_qr_code'),
                       # url(r'^image/$', 'thumbapp.views.image'),
                       url(r'^append_tags/$', 'obj_sys.obj_tagging.handle_append_tags_request'),
                       url(r'^query/$', 'obj_sys.views.query'),
                       url(r'^operations/', 'obj_sys.views.do_operation'),
                       url(r'^do_json_operation/$', 'obj_sys.views.do_json_operation'),
                       url(r'^remove_tag/$', 'obj_sys.obj_tagging.remove_tag'),
                       url(r'^add_tag/$', 'obj_sys.obj_tagging.add_tag'),
                       url(r'^get_tags/$', 'obj_sys.obj_tagging.get_tags'),
                       url(r'^tag_list/$', ListView.as_view(
                           queryset=Tag.objects.all(),
                           context_object_name='tagged_items',
                           template_name='obj_sys/pane.html')),
                       (r'^api/ufsobj/', include(ufs_obj_resource.urls)),
                       (r'^api/ufs_obj_in_tree/', include(ufs_obj_in_tree_resource.urls)),
                       (r'^tree_raw/', ItemTreeView.as_view(template_name='obj_sys/mptt_tree.html')),
                       (r'^tree/', ItemTreeView.as_view(template_name='obj_sys/mptt_tree_content_only.html')),
                       url(r'^ufs_obj_rest/(?P<pk>[0-9]+)/$', get_detail_api_class(UfsObj).as_view()),
                       url(r'^mptt_tree_view/', login_required(ItemTreeView.as_view(
                           default_level=2,
                           ufs_obj_type=2,
                           template_name='obj_sys/jquery_sortable_list.html'))),
                       # (r'^api/tag/', include(tag_resource.urls)),
                       # url(r'^$', 'desktop.filemanager.views.index'),
                       # url(r'^.+$', 'desktop.filemanager.views.handler'),
                       # url(r'^homepage_all/$', 'obj_sys.views.homepage'),
                       #  url(r'^ufs/', include(obj_views.urls)),
                       )
