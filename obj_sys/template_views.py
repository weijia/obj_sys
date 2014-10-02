from django.contrib import auth
from django.core.context_processors import csrf
from django.views.generic import TemplateView
from djangoautoconf.django_utils import retrieve_param
from models_ufs_obj import UfsObj

__author__ = 'weijia'


class HomepageTemplateView(TemplateView):
    template_name = 'obj_sys/listing_with_description_in_bootstrap.html'
    http_method_names = ["post", "get"]

    def get_context_data(self, **kwargs):
        context = super(HomepageTemplateView, self).get_context_data(**kwargs)
        data = retrieve_param(self.request)
        ufs_obj_type = int(data.get("type", "1"))
        objects = UfsObj.objects.filter(user=auth.get_user(self.request), valid=True,
                                        ufs_obj_type=ufs_obj_type).order_by('-timestamp')
        if "keyword" in data:
            objects = objects.filter(descriptions__content__contains=data["keyword"])
        c = {"objects": objects, "request": self.request, "title": "My bookmarks",
             "email": "richardwangwang@gmail.com", "author": "Richard"}
        c.update(csrf(self.request))
        context.update(c)
        return context