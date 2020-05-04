from django.contrib import admin
from django.urls import path
from MyNetApp import views
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.MyViewClass.as_view(),name = 'show_signup_page'),
    path('login/',TemplateView.as_view(template_name='pages/login.html')),
]
