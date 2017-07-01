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
    # 'endless_pagination',
    'el_pagination',
    'crispy_forms',
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
)

# MIDDLEWARE_CLASSES += (
#     'reversion.middleware.RevisionMiddleware',
# )
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 20,
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.backends.DjangoFilterBackend', )
}