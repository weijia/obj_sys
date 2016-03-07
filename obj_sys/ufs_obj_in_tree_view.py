from django.core.context_processors import csrf
from django.views.generic import TemplateView
from djangoautoconf.django_utils import retrieve_param
from models_mptt import UfsObjInTree


class TreeView(TemplateView):
    item_class = UfsObjInTree
    default_level = 2

    def __init__(self, **kwargs):
        super(TreeView, self).__init__(**kwargs)
        self.tree_items = None
        self.root_pk = -1

    def get_context_data(self, **kwargs):
        # context = super(AddTagTemplateView, self).get_context_data(**kwargs)
        context = {}
        self.init_tree_items()
        self.get_final_query_set()
        c = {"user": self.request.user, "nodes": self.tree_items}
        c.update(csrf(self.request))
        context.update(c)
        # log = logging.getLogger(__name__)
        # log.error(context)
        return context

    def get_final_query_set(self):
        pass

    def init_tree_items(self):
        data = retrieve_param(self.request)
        if "root" in data:
            self.root_pk = data["root"]
            self.tree_items = self.get_children(self.root_pk)
        else:
            self.tree_items = self.item_class.objects.filter(level__lt=self.default_level)

    def get_children(self, root_pk):
        root = self.item_class.objects.filter(pk=root_pk)
        tree_items = self.item_class.objects.get_queryset_descendants(root).filter(
                level__lt=root[0].level + self.default_level + 1)
        return tree_items


class ItemTreeView(TreeView):
    ufs_obj_type = None

    def get_final_query_set(self):
        if self.ufs_obj_type is not None:
            self.tree_items = self.tree_items.filter(ufs_obj_type=self.ufs_obj_type)
