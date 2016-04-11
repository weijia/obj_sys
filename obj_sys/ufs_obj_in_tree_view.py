from mptt_tree_view.views import TreeView
from obj_sys.models_ufs_obj import UfsObj


class ItemTreeView(TreeView):
    ufs_obj_type = None
    item_class = UfsObj

    def get_final_query_set(self):
        if self.ufs_obj_type is not None:
            self.tree_items = self.tree_items.filter(ufs_obj_type=self.ufs_obj_type)
