import logging
import os
import threading
from django.http import HttpResponse
from djangoautoconf.django_utils import retrieve_param

log = logging.getLogger(__name__)


class StarterThread(threading.Thread):
    def __init__(self, path):
        super(StarterThread, self).__init__()
        self.path = path

    def run(self):
        os.startfile('"' + self.path + '"')


def start(request):
    data = retrieve_param(request)
    full_path = data["full_path"]
    log.debug(full_path)
    try:
        ext = os.path.splitext(full_path)[1]
    except:
        ext = ''
    if True:  #try:
        if ext in ['.bat', '.py']:
            from services.sap.launcher_sap import Launcher

            Launcher().start_app_with_exact_full_path_and_param_list_no_wait(full_path)
            #raise "stop here"
            #return "app"
        else:
            StarterThread(full_path).start()
            #raise "stop there"
            #return "doc"
        response = '{"result": "ok", "path": %s}' % full_path
    else:#except:
        response = '{"result": "failed", "path": %s}' % full_path
    return HttpResponse(response, mimetype="application/json")


def remove_thumb_for_paths(request):
    data = retrieve_param(request)
    cnt = 0
    if "path" in data:
        path = data["path"]
        res = []
        from thumbapp.models import ThumbCache

        for i in ThumbCache.objects.filter(obj__full_path__contains=path):
            if cnt < 100:
                res.append(i.obj.full_path)
            else:
                break
            cnt += 1
        ThumbCache.objects.filter(obj__full_path__contains=path).delete()
        return HttpResponse(res, mimetype="application/json")