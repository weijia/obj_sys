# Create your models here.
from models_mptt import *
from models_obj_rel import *

try:
    import tagging
    tagging.register(UfsObj)
except ImportError:
    pass
