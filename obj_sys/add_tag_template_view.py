from django.core.context_processors import csrf
from django.views.generic import TemplateView
from djangoautoconf.django_utils import retrieve_param
from ufs_tools.string_tools import SpecialEncoder
from models import UfsObj
from obj_tagging import append_tags_and_description_to_url
import obj_tools


class AddTagTemplateView(TemplateView):
    template_name = 'obj_sys/tagging.html'
    http_method_names = ["post", "get"]

    def __init__(self, **kwargs):
        super(AddTagTemplateView, self).__init__(**kwargs)
        self.encoding = None
        self.tags = []
        self.tagged_urls = []
        self.stored_url = []
        self.listed_urls = []
        self.is_submitting_tagging = False
        self.ufs_obj_type = UfsObj.TYPE_UFS_OBJ

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AddTagTemplateView, self).get_context_data(**kwargs)
        urls_with_tags = self.get_requesting_url_and_tag_pair()

        c = {"user": self.request.user, "close_flag": self.is_submitting_tagging, "urls_with_tags": urls_with_tags,
             "new_url_input": False}
        if 0 == len(urls_with_tags):
            c["new_url_input"] = True
        c.update(csrf(self.request))
        context.update(c)
        # log = logging.getLogger(__name__)
        # log.error(context)
        return context

    def get_requesting_url_and_tag_pair(self):
        data = retrieve_param(self.request)
        self.update_stored_url()

        self.process_parameters(data)

        decoder = SpecialEncoder()
        for query_param_list in data.lists():
            if query_param_list[0] == "url":
                all_urls = []
                for submitted_url in query_param_list[1]:
                    all_urls.append(decoder.decode(submitted_url))
                self.stored_url.extend(all_urls)
                for submitted_url in self.stored_url:
                    if not (submitted_url in self.listed_urls):
                        # print query_param_list, urls
                        self.listed_urls.append(submitted_url)
            if query_param_list[0] == 'selected_url':
                self.is_submitting_tagging = True
                for submitted_url in query_param_list[1]:
                    self.tag_url(submitted_url)
        self.request.session["saved_urls"] = self.listed_urls
        urls_with_tags = self.get_urls_with_tags()
        return urls_with_tags

    def process_parameters(self, data):
        self.update_ufs_obj_type(data)
        self.retrieve_encoding(data)
        self.update_tags(data)

    def update_ufs_obj_type(self, data):
        if "ufs_obj_type" in data:
            self.ufs_obj_type = data["ufs_obj_type"]

    def update_tags(self, data):
        if "tags" in data:
            self.tags = data["tags"]

    def update_stored_url(self):
        # Load saved submitted_url
        if "saved_urls" in self.request.session:
            self.stored_url = self.request.session["saved_urls"]

    def retrieve_encoding(self, data):
        if "encoding" in data:
            self.encoding = data["encoding"]
        else:
            self.encoding = "utf8"

    @staticmethod
    def get_url_tags(url_for_ufs_obj):
        tags = []
        if obj_tools.is_web_url(url_for_ufs_obj):
            obj_qs = UfsObj.objects.filter(ufs_url=url_for_ufs_obj)
        else:
            full_path = obj_tools.get_full_path_for_local_os(url_for_ufs_obj)
            obj_qs = UfsObj.objects.filter(full_path=full_path)
            # print obj_qs.count()
        if 0 != obj_qs.count():
            # print 'object exists'
            for obj in obj_qs:
                # print obj.tags
                tags.extend(obj.tags)
        return tags

    def get_urls_with_tags(self):
        class UrlTagPair:
            def __init__(self, url, tags):
                self.url = url
                self.tags = tags

        urls_with_tags = []
        for listed_url in self.listed_urls:
            tags_for_existing_url = self.get_url_tags(listed_url)
            urls_with_tags.append(UrlTagPair(listed_url, tags_for_existing_url))
        return urls_with_tags

    def tag_url(self, url_to_tag, ufs_obj_type=UfsObj.TYPE_UFS_OBJ):
        if not (url_to_tag in self.tagged_urls):
            self.tagged_urls.append(url_to_tag)
            append_tags_and_description_to_url(self.request.user, url_to_tag,
                                               self.tags, "manually added item", ufs_obj_type)
