from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Item,LastPostID
from datetime import datetime

class Res:
    def __init__(self):
        self.realname = ""
        self.content = ""


## init-need now is no-use
def zbList(request):
    #if not request.is_ajax():
    #    return HttpResponse(None)
    if LastPostID.objects.all() is None:
        LastPostID.objects.create(postdt = datetime.today(), postid = 1)
    length = len(LastPostID.objects.all())
    last = LastPostID.objects.all()[length - 1]
    # the last post datetime
    last_dt = last.postdt
    # set the name_dict
    name_dict = {}
    lst = [x for x in Item.objects.all() if x.dt > last_dt]
    # set the zblist above owing to the need
    zblist = []
    for x in lst:
        i_dir = {}
        i_dir.setdefault("realname", x.realname)
        i_dir.setdefault("content", x.content)
        zblist.append(i_dir)
    name_dict.setdefault('zblist', zblist)

    LastPostID.objects.create(postdt=datetime.today(), postid=length+1)
    return JsonResponse(name_dict)

def history(request):
    name_dict = {}
    lst = Item.objects.all()
    # set the zblist
    zblist = []
    for x in lst:
        i_dir = {}
        i_dir.setdefault("realname", x.realname)
        i_dir.setdefault("content", x.content)
        zblist.append(i_dir)
    return render(request, "resource.html", {"zblist":zblist})

def add_ls(request):
    if LastPostID.objects.all() is None:
        LastPostID.objects.create(postdt = datetime.today(), postid = 1)
    length = len(LastPostID.objects.all())
    last = LastPostID.objects.all()[length - 1]
    last_dt = last.postdt
    lst = [x for x in Item.objects.all() if x.dt > last_dt]
    add_ls = []
    for x in lst:
        i_dir = {}
        i_dir.setdefault("realname", x.realname)
        i_dir.setdefault("content", x.content)
        add_ls().append(i_dir)
    test = "test-for-ul-get-add"
    return render(request, "ul.html", {"add_ls":add_ls, "test":test})

def home(request):

    test = "test"

    return render(request, "index.html", {"t":test})

def test_ajax(request):
    dict = [
        {"optionKey": "1", "optionValue": "Canon in D"},
        {"optionKey": "2", "optionValue": "Wind Song"},
        {"optionKey": "3", "optionValue": "Wings"}
    ]
    return JsonResponse({"dict":dict})
