# Create your models here.
from models_obj_rel import *
from models_ufs_obj import *



try:
    # apps.py
    from django.apps import AppConfig
    try:
        import tagging

        tagging.register(UfsObj)
    except ImportError:
        pass
except ImportError:
    try:
        import tagging
        tagging.register(UfsObj)
    except ImportError:
        pass
except ImportError:
    pass
