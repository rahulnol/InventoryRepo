from django.contrib import admin
from django.urls import path
from MyNetApp import views
from django.views.generic import TemplateView
from django.conf.urls import include,re_path

from django.conf import settings
from django.conf.urls.static import static
from venue import views as venue_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.SignupView.as_view(),name = 'show_signup_page'),
    path('login/',TemplateView.as_view(template_name='pages/login.html')),
    # path('dashboard/',TemplateView.as_view(template_name='base_dashboard.html'), name='dashboard'),
    path('dashboard/',venue_view.VenueProfileView.as_view(), name='dashboard'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('validatelogin/',views.validateLogin),
    path('venue/', include('venue.urls')),
    #path('validatelogin/',views.ValidateLogin.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
