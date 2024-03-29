"""login_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from login_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("index/",views.index),
    path("login1/",views.login1),
    #path('login1/',views.login1)
    path("event_manage/",views.event_manage),
    path("guest_manage/",views.guest_manage),
    path("accounts/login/",views.index),
   # path("sign_index/(?P<eid>[0-9]+)/$",views.sign_index),
    re_path("sign_index/(?P<eid>[0-9]+)/", views.sign_index),
    re_path("sign_index_action/(?P<eid>[0-9]+)/", views.sign_index_action),
    #re_path('sign_index_action/<int:event_id>/', views.sign_index_action),
    #re_path(r"^sign_index_action/(?P<eid>[0-9]+)/$", views.sign_index_action),
    path('logout/', views.logout),
   # url(r'^search_name/$', views.search_name),
    path("search_name/",views.search_name),
    #url(r'^search_realname/$', views.search_realname),
    path("search_realname/",views.search_realname),

]
