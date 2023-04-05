from django.shortcuts import render

# importing http response 
from django.http import HttpResponse
# the httpResponse, sends the Http response from the django server to the client 
# the response is written in the views.py file 


def index(request) :
    # the index function is the name of the 
    return HttpResponse('This is an HttpResponse')