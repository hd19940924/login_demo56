from django.shortcuts import render
from django.http import HttpResponse
import json
#from django.shortcuts import render_to_response
# Create your views here.
def index(request):
    return  HttpResponse("hello django")
def login(request):
    if request.method == "POST":
        result = {}
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        # if username=="admin" and password=="123456":
        result["user"] = username
        result["psw"] = password
        result = json.dumps(result)
        return HttpResponse(result, content_type="application/json;charset=utf-8")
    else:

           return  render(request,"login.html")

