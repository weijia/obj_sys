#from django.conf.urls import patterns, include, url
#import libsys
from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from tagging.models import Tag
from api import UfsObjResource, UfsObjInTreeResource
from add_tag_template_view import AddTagTemplateView
from add_tag_template_view_local import AddTagTemplateViewLocal
from ufs_obj_in_tree_view import UfsObjInTreeView
from rss import LatestEntriesFeed


ufs_obj_resource = UfsObjResource()
ufs_obj_in_tree_resource = UfsObjInTreeResource()
#tag_resource = TagResource()

urlpatterns = patterns('',
    url(r'^tagging/$', login_required(AddTagTemplateView.as_view())),
    url(r'^tagging_local/$', login_required(AddTagTemplateViewLocal.as_view())),
    url(r'^tagging/(?P<news_item_pk>\d+)/$', login_required(AddTagTemplateView.as_view()), name="news-item"),
    url(r'^manager/$', 'obj_sys.views.manager'),
    url(r'^listing/$', 'obj_sys.views.listing'),
    url(r'^homepage/$', 'obj_sys.views.listing_with_description'),
    (r'^latest/feed/$', LatestEntriesFeed()),
    #url(r'^qrcode/$', 'thumbapp.views.gen_qr_code'),
    #url(r'^image/$', 'thumbapp.views.image'),
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
    (r'^tree/', UfsObjInTreeView.as_view(template_name='obj_sys/mptt_tree.html')),
    #(r'^api/tag/', include(tag_resource.urls)),
    #url(r'^$', 'desktop.filemanager.views.index'),
    #url(r'^.+$', 'desktop.filemanager.views.handler'),
    #url(r'^homepage_all/$', 'obj_sys.views.homepage'),
)