from django.urls import path
from venue import views

urlpatterns = [
    path('profile/',views.VenueProfileView.as_view()),
]