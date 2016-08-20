__author__ = 'weijia'


INSTALLED_APPS += (
    'mptt',
    'reversion',
    'django_mptt_admin',
    'tagging',
    'ajax_select',
    'django_extensions',
    'geoposition',
    'obj_sys',
    # "obj_sys.apps.ObjSysConfig",
    'endless_pagination',
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
)

# MIDDLEWARE_CLASSES += (
#     'reversion.middleware.RevisionMiddleware',
# )
