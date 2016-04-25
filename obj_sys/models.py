# Create your models here.
from models_obj_rel import *
from models_ufs_obj import *


try:
    import tagging
    tagging.register(UfsObj)
except ImportError:
    pass
