# Create your views here.
from obj_tagging import *
from obj_operator import ObjOperator, ObjListOperator, handle_operation_request
from djangoautoconf.django_utils import retrieve_param
from models import UfsObj
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


log = logging.getLogger(__name__)


@login_required
def manager(request):
    data = retrieve_param(request)
    c = {"user": request.user, "tree": {"name": "left_tree", "url": "/custom_collections/jstree/?node="}}
    c.update(csrf(request))
    return render_to_response('obj_sys/manager.html', c)


def query(request):
    c = {"user": request.user}
    c.update(csrf(request))
    return render_to_response('obj_sys/query.html', c)


def rm_objects_for_path(request):
    data = retrieve_param(request)
    cnt = 0
    if "ufs_url" in data:
        res = []
        prefix = data["ufs_url"]
        if prefix[-1] != "/":
            prefix += "/"
        for i in UfsObj.objects.filter(ufs_url__startswith=prefix):
            if cnt < 100:
                res.append(i.full_path)
            else:
                break
            cnt += 1
            #Remove tags first?
        #TaggedItem.objects.filter(object__ufs_url__startswith=data["ufs_url"]).delete()
        UfsObj.objects.filter(ufs_url__startswith=prefix).delete()
        return HttpResponse(res, mimetype="application/json")


def listing(request):
    objects = UfsObj.objects.all()
    return render_to_response('obj_sys/listing.html', {"objects": objects, "request": request},
                              context_instance=RequestContext(request))


@login_required
def listing_with_description(request):
    data = retrieve_param(request)
    ufs_obj_type = int(data.get("type", "1"))
    objects = UfsObj.objects.filter(user=request.user, valid=True, ufs_obj_type=ufs_obj_type).order_by('-last_modified')
    return render_to_response('obj_sys/listing_with_description_in_bootstrap.html',
                              {"objects": objects, "request": request, "title": "My bookmarks",
                               "email": "richardwangwang@gmail.com", "author": "Richard"},
                              context_instance=RequestContext(request))


@login_required
def do_operation(request):
    data = retrieve_param(request)
    if ("cmd" in data) and ("pk" in data):
        operator = ObjOperator(int(data["pk"]))
        getattr(operator, data["cmd"])()
    next_url = "/obj_sys/homepage/"
    if "next_url" in data:
        next_url = data["next_url"]
    return HttpResponseRedirect(next_url)


@login_required
def do_json_operation(request):
    return handle_operation_request(request)