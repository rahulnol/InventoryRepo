from django.urls import path
from venue import views
from django.conf.urls import re_path, include

urlpatterns = [
    path('profile/', views.VenueProfileView.as_view()),
    path('modifyspace/', views.ModifySpace.as_view()),
    re_path('modifyspace/(?P<myid>\d+)/$', views.ModifySpace.as_view()),

]
