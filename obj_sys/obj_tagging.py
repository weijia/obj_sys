import json
import logging
import threading
import uuid

from compat import JsonResponse
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
import django.utils.timezone as timezone
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from ufs_local_obj import UfsUrlObj, UfsLocalObjSaver
from tagging.models import Tag
from djangoautoconf.django_utils import retrieve_param
from djangoautoconf.req_with_auth import RequestWithAuth
import obj_tools
from models import UfsObj
from models import Description
from view_utils import get_ufs_obj_from_ufs_url


def is_barcode(url):
    if obj_tools.is_ufs_url(url):
        protocol = obj_tools.get_protocol(url)
        if protocol in ["bar"]:
            return True
    return False


def get_or_create_objects_from_remote_or_local_url(web_url_or_qt_file_url, user, ufs_obj_type=UfsObj.TYPE_UFS_OBJ):
    """
    Create object if url is not exist, otherwise use the existing one. So if an existing url is passed in
    the existing item will be updated instead of creating a new one.
    :param web_url_or_qt_file_url:
    :param user:
    :param ufs_obj_type:
    """
    # Tag object
    if obj_tools.is_web_url(web_url_or_qt_file_url) or is_barcode(web_url_or_qt_file_url):
        obj_saver = UfsUrlObj(web_url_or_qt_file_url, user)
    else:
        obj_saver = UfsLocalObjSaver(user)
        obj_saver.init_with_qt_url(web_url_or_qt_file_url)
    return obj_saver.filter_or_create()


def append_tags_and_description_to_url(user, web_url_or_qt_file_url, str_of_tags, description,
                                       ufs_obj_type=UfsObj.TYPE_UFS_OBJ):
    if obj_tools.is_web_url(web_url_or_qt_file_url) or is_barcode(web_url_or_qt_file_url):
        obj_saver = UfsUrlObj(web_url_or_qt_file_url, user, ufs_obj_type=ufs_obj_type)
    else:
        obj_saver = UfsLocalObjSaver(user)
        obj_saver.init_with_qt_url(web_url_or_qt_file_url)
    obj_saver.get_or_create()
    description_obj, created = Description.objects.get_or_create(content=description)
    obj_saver.tag_app = 'user:' + user.username
    obj_saver.append_tags(str_of_tags)
    obj_saver.add_description(description_obj)


@csrf_exempt
def handle_append_tags_request(request):
    req_with_auth = RequestWithAuth(request)
    if not req_with_auth.is_authenticated():
        res = req_with_auth.get_error_dict()
        res["result"] = "error"
        return JsonResponse(res)

    tags = req_with_auth.data.get("tags", None)
    description = req_with_auth.data.get("description", None)
    ufs_obj_type = int(req_with_auth.data.get("ufs_obj_type", "1"))
    added_cnt = 0
    for query_param_list in req_with_auth.data.lists():
        if query_param_list[0] == "selected_url":
            for url in query_param_list[1]:
                append_tags_and_description_to_url(request.user, url, tags, description, ufs_obj_type)
                added_cnt += 1
    return JsonResponse({"result": "OK", "added": "%d" % added_cnt})


def remove_tag(request):
    data = retrieve_param(request)
    if ('ufs_url' in data) and ('tag' in data):
        # print data['ufs_url']
        obj_list = UfsObj.objects.filter(ufs_url=data['ufs_url'])
        if 0 != obj_list.count():
            tags = obj_list[0].tags
            tag_name = []
            for tag in tags:
                if tag.name != data['tag']:
                    tag_name.append(tag.name)
            obj_list[0].tags = ','.join(tag_name)
            print tag_name
            return JsonResponse({"result": "remove tag done"})
    return JsonResponse({"result": "not enough params"})


def get_tags(request):
    tag_list = Tag.objects.usage_for_model(UfsObj)
    tag_name_list = []
    for i in tag_list:
        tag_name_list.append(i.name)
    return HttpResponse(json.dumps(tag_name_list))


def add_tag(request):
    data = retrieve_param(request)
    if ('ufs_url' in data) and ('tag' in data):
        obj = get_ufs_obj_from_ufs_url(data['ufs_url'])
        Tag.objects.add_tag(obj, data["tag"], tag_app='user:' + request.user.username)
        return HttpResponse('{"result": "added tag: %s to %s done"}' % (data["tag"], data["ufs_url"]),
                            mimetype="application/json")
    return JsonResponse({"result": "not enough params"})
