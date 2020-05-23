from django.contrib import admin
from django.urls import path
from django.conf.urls import include,re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/',include('main.urls'))
]
