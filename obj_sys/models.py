# Create your models here.
from models_mptt import *


try:
    import tagging
    tagging.register(UfsObj)
except ImportError:
    pass
