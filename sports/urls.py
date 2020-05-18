from django.urls import path, re_path
from .views import AddonView
urlpatterns = [
    path('addon/',AddonView.as_view()),
    re_path('addon/(?P<pk>\w+)$', AddonView.as_view()),
]
