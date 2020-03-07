
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',  views.index, name='index')
]
