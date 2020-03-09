
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from inventory.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', index, name='index')
]
