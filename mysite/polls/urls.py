# the urls.py file in the polls app. maps the urls of the app
# this does not include the urls of the project or other apps in the project 
# and only maps the urls in this current app only 

# importing path from urls 
from django.urls import path 

from . import views
# the '.', means the current durectory, so views.py is inside the same directory as urls.py ( of the app ), so
# we use teh '.' 

app_name = 'polls'
# when django, finds the polls urls in the mysite/urls, it will find  the namespace = 'polls'
# so, initializing the app_name = 'polls', will make it verify, that this urls is of the polls app


urlpatterns = [
    path("" , views.IndexView.as_view() , name = "index"),
    path("<int:pk>/" ,views.DetailView.as_view() , name = "detail"),
    path("<int:pk>/results/" , views.ResultsView.as_view() , name = "result"),
    path("<int:question_id>/vote/" , views.vote , name = "vote"),
    path("login/" ,  views.login , name = "login")
]

# the path() function has 3 paramters 
# 1. The path of the app. Here it is blank, meaning at the base ( root ) directory of the app 
# 2. views.index -> means the index function from the views file 
# 3. name = "index" , means the name of the end path ( appearing on the url of the browser ), here we are setting the 
# name as index , meaning /app/index
