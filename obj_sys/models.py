# Create your models here.
from models_mptt import *
from models_obj_rel import *


try:
    # apps.py
    from django.apps import AppConfig
except ImportError:
    try:
        import tagging
        tagging.register(UfsObj)
    except ImportError:
        pass
except ImportError:
    pass
