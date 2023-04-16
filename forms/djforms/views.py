from django.shortcuts import render

from django.http import HttpResponse

# importing the myForm
from .forms import myForm

from .models import formModel

# Create your views here.
def homeView(request) : 
    # displaying the myForm here
    print("Inside the homeView ")

    if request.method=='GET' : 
        form = myForm()

        return render(request , 'main.html' , {"form" : form})

    if request.method=='POST' : 

        formData = myForm(request.POST)

        # checking if the form is valid
        if formData.is_valid() :
            # otaining the values 
            name = formData.cleaned_data['name']
            address = formData.cleaned_data['address']
            choice = formData.cleaned_data['choice']
            print(name)
            print(address)
            print(choice)

        else : 
            return HttpResponse("The form is invalid, retry")

        return HttpResponse("THis is a string")  