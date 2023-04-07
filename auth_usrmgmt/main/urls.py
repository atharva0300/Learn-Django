from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    # path for the homepage
    # and inititializing the home view for the url
    path('accounts/' , include('django.contrib.auth.urls')),
    path('' , TemplateView.as_view(template_name = 'home.html') , name = 'home'),
    path('social-auth/' , include('social_django.urls' , namespace='social'))
]