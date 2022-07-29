from django.shortcuts import render
from django.http import HttpResponse
import json
#from django.shortcuts import render_to_response
# Create your views here.
from django.http import HttpResponseRedirect
from login_app.models import Event,Guest
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import  render,get_object_or_404,get_object_or_404, get_list_or_404
def index(request):
    return  render(request,"index.html")

def login1(request):
    if request.method == "POST":
        result = {}
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
        #if username=="admin" and password=="123456":
            #return HttpResponse("login success")
            #return  HttpResponseRedirect("/event_manage/")
            response= HttpResponseRedirect("/event_manage/")
            #response.set_cookie("user",username,3600)
            request.session["user"]=username
            return response
        else:
              return  render(request,"index.html",{"error":"uesrname or password error!"})
@login_required
def event_manage(request):
    #username= request.COOKIES.get("user","")
    #username=request.session.get("user","")
    #return  render(request,"event_manage.html",{"user":username})
    event_list = Event.objects.all()
    username = request.session.get('user', '')
    return render(request, "event_manage.html", {"user": username, "events": event_list})

""""@login_required
def guest_manage(request):
    #username= request.COOKIES.get("user","")
    #username=request.session.get("user","")
    #return  render(request,"event_manage.html",{"user":username})
    guest_list = Guest.objects.all()
    username = request.session.get('user', '')
    return render(request, "guest_manage.html", {"user": username, "guests": guest_list})"""""
@login_required

def guest_manage(request):

    guest_list = Guest.objects.all()

    username = request.session.get('username', '')

    paginator = Paginator(guest_list, 2)

    page = request.GET.get('page')

    try:

        contacts = paginator.page(page)

    except PageNotAnInteger:

        # 如果页数不是整型, 取第一页.

        contacts = paginator.page(1)

    except EmptyPage:

        # 如果页数超出查询范围，取最后一页

        contacts = paginator.page(paginator.num_pages)

    return render(request, "guest_manage.html", {"user": username, "guests": contacts})
# 签到动作
@login_required

def sign_index(request, eid):
    username = request.session.get('user', '')

    event = get_object_or_404(Event, id=eid)
    guest_list = len(get_list_or_404(Guest, event_id=eid))
    guest_sign = len(get_list_or_404(Guest, event_id=eid, sign=1))

    return render(request, 'sign_index.html',{"user": username, "event": event} )
# 签到动作
"""@login_required
def sign_index_action(request,eid):#/sign_index_action/
    event = get_object_or_404(Event, id=eid)
    phone = request.POST.get("phone","")
    print(phone)
    result = Guest.objects.filter(phone=phone)
    if not result:
        return render(request, 'sign_index.html', {'event':event, 'hint':'phone error.'})

    result = Guest.objects.filter(phone=phone, event_id = eid)
    if not result:
        return render(request, 'sign_index.html', {'event':event, 'hint':'event id or phone error.'})

    result = Guest.objects.filter(phone=phone, event_id = eid)
    if result.sign:
        return render(request, 'sign_index.html', {'event':event, 'hint':'user has sign in.'})
    else:
        Guest.objects.filter(phone=phone, event_id = eid).update(sign='1')
        return render(request, 'sign_index.html', {'event':event, 'hint':'sign in success!', 'guest':result})"""
# 签到动作
@login_required
def sign_index_action(request,eid):
    username = request.session.get('user', '')
    event = get_object_or_404(Event, id=eid)
    guest_list = len(get_list_or_404(Guest, event_id=eid))
    guest_sign = len(get_list_or_404(Guest, event_id=eid, sign=1))
    phone = request.POST.get("phone","")
    print(phone)
    result = Guest.objects.filter(phone=phone)
    if not result:
        return render(request, 'sign_index.html', {'user': username,'event':event, 'hint':'phone error.','guest_list': guest_list, 'guest_sign': guest_sign})

    result = Guest.objects.filter(phone=phone, event_id = eid)
    if not result:
        return render(request, 'sign_index.html', {'user': username,'event':event, 'hint':'event id or phone error.','guest_list': guest_list, 'guest_sign': guest_sign})

    result = Guest.objects.get(phone=phone, event_id = eid)
    if result.sign:
        return render(request, 'sign_index.html', {'user': username,'event':event, 'hint':'user has sign in.','guest_list': guest_list, 'guest_sign': guest_sign})
    else:
        Guest.objects.filter(phone=phone, event_id = eid).update(sign='1')
        guest_sign = guest_sign + 1
        return render(request, 'sign_index.html', {'user': username,'event':event, 'hint':'sign in success!', 'guest':result,'guest_list': guest_list, 'guest_sign': guest_sign})
@login_required
def logout(request):
    auth.logout(request) # 退出登陆
    response = HttpResponseRedirect('/index/')
    return response
@login_required
def search_name(request):
    username = request.session.get('user', '')
    # 通过get()方法获取name关键字
    search_name = request.GET.get("name", "")
    # 在Event中匹配name字段
    event_list = Event.objects.filter(name__contains=search_name)
    # 将匹配到的发布会列表注意这里是列表不是对象，返回给客户端
    return render(request, "event_manage.html", {"user":username, "events":event_list})
# 嘉宾名称搜索
@login_required
def search_realname(request):
    username = request.session.get('user', '')
    search_realname = request.GET.get("realname", "")
    # 注意这里需要将过滤器的名称也修改为realname__contains
    guest_list = Guest.objects.filter(realname__contains=search_realname)
    return render(request, "guest_manage.html", {"user": username, "guests": guest_list})