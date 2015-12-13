from django.core.context_processors import csrf
from django.views.generic import TemplateView
from djangoautoconf.django_utils import retrieve_param
from models_mptt import UfsObjInTree


class ItemTreeView(TemplateView):
    item_class = UfsObjInTree
    default_level = 2

    def get_context_data(self, **kwargs):
        # context = super(AddTagTemplateView, self).get_context_data(**kwargs)
        context = {}
        data = retrieve_param(self.request)
        if "root" in data:
            root = self.item_class.objects.filter(pk=data["root"])
            tree_items = self.item_class.objects.get_queryset_descendants(root).filter(
                level__lt=root[0].level+self.default_level)
        else:
            tree_items = self.item_class.objects.filter(level__lt=self.default_level)

        c = {"user": self.request.user, "nodes": tree_items}
        c.update(csrf(self.request))
        context.update(c)
        # log = logging.getLogger(__name__)
        # log.error(context)
        return context
