from django.contrib import admin

# Register your models here.
from django.contrib import admin
from login_app.models import Event,Guest

# Register your models here.
# 这些代码通知Admin管理工具为这些模块提供界面
class EventAdmin(admin.ModelAdmin):
    list_display=['id','name', 'status', 'address', 'start_time']
    search_fields = ['name']  # 搜索栏
    list_filter = ['status']  # 过滤器

class GuestAdmin(admin.ModelAdmin):
    list_display=['realname','phone', 'email', 'sign', 'create_time', 'event']
    search_fields = ['realname', 'phone']  # 搜索栏
    list_filter = ['sign']  # 过滤器

admin.site.register(Event, EventAdmin)
admin.site.register(Guest, GuestAdmin)
