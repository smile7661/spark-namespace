from django.urls import path
from django.contrib import admin

app_name = 'WeeklyReport'

admin.site.site_header = '周报管理系统'

urlpatterns = [
    path('', admin.site.urls, name='django登陆')
]
