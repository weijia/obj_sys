__author__ = 'weijia'


INSTALLED_APPS += (
    'mptt',
    'django_mptt_admin',
    'tagging',
    'geoposition',
    'obj_sys',
    # "obj_sys.apps.ObjSysConfig",
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
)