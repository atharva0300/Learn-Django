from django.urls import path

from . import views
from djforms.views import homeView

urlpatterns =[
    path('' , view = homeView , name = 'homeView' )
]