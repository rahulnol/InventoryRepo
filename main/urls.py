from django.urls import path
from django.conf.urls import include,re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('',TemplateView.as_view(template_name='main/base.html'))
]