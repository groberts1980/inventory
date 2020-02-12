
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',  views.index, name='index')
]
