from django.core.context_processors import csrf
from django.views.generic import TemplateView
from djangoautoconf.django_utils import retrieve_param
from models_mptt import UfsObjInTree


class UfsObjInTreeView(TemplateView):
    def __init__(self, **kwargs):
        super(UfsObjInTreeView, self).__init__(**kwargs)

    def get_context_data(self, **kwargs):
        # context = super(AddTagTemplateView, self).get_context_data(**kwargs)
        context = {}
        data = retrieve_param(self.request)
        if "root" in data:
            root = UfsObjInTree.objects.filter(pk=data["root"])
            tree_items = UfsObjInTree.objects.get_queryset_descendants(root)
        else:
            tree_items = UfsObjInTree.objects.all()

        c = {"user": self.request.user, "nodes": tree_items}
        c.update(csrf(self.request))
        context.update(c)
        # log = logging.getLogger(__name__)
        # log.error(context)
        return context
