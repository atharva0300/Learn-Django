# the urls.py file in the polls app. maps the urls of the app
# this does not include the urls of the project or other apps in the project 
# and only maps the urls in this current app only 

# importing path from urls 
from django.urls import path 

from . import views
# the '.', means the current durectory, so views.py is inside the same directory as urls.py ( of the app ), so
# we use teh '.' 

urlpatterns = [
    path("" , views.index , name = "index"),
    path("<int:question_id>/" ,views.detail , name = "detail"),
    path("<int:question_id>/results/" , views.result , name = "result"),
    path("<int:question_id>/votes/" , views.vote , name = "vote")
]

# the path() function has 3 paramters 
# 1. The path of the app. Here it is blank, meaning at the base ( root ) directory of the app 
# 2. views.index -> means the index function from the views file 
# 3. name = "index" , means the name of the end path ( appearing on the url of the browser ), here we are setting the 
# name as index , meaning /app/index
