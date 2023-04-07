from django.shortcuts import render, redirect

# importing django authentication 
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages

from django.http import HttpResponse

# importing the form 
from .forms import SignUpForm


# Create your views here.
def home(request) : 
    # check to see if a person is loggin in
    if(request.method=="POST") : 

        # getting the data filled in the form 
        username = request.POST['username']
        password = request.POST['password']

        # authenticate the user 
        user = authenticate(request , username = username  , password = password)
        # passing the username and the password into the authenticate function

        if(user is not None ) :
            # if there is a user present 
            # then 
            login(request , user)
            # login the user 
            # ie- setting the user as loggin
            # the user ( which contains the authenticated username and password ) is passed to the login function
            messages.success(request , 'You have been Loggedin!')
            print('There is an error logging in')
            return redirect('home')
            # redirect the page to the homepage  
        
        else : 
            # if the user is not present, then 
            messages.success(request , 'There was an error in logging in')
            return redirect('home')

    
    return render(request , 'home.html' , {})

    # flash up a form if the user is not logged in
    # else, if logged in -> then show the crm


# view for logout 
def logout_user(request) : 
    # logging out the user

    # only appear the logout, when the user is loggedin
    # else no 
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')


# for registering the user 
def register_user(request) : 
    # checking if it is a post method 
    if (request.method == 'POST') : 
        form = SignUpForm(request.POST)
        # passing the data of the request form 
        # to the SignUpForm class
        # it get's initialized 

        if form.is_valid() : 
            form.save()
            # authenticate and login 
            username = form.cleaned_data['username']
            # form.cleaned_data takes the data from the form
            # and provides the username 

            password = form.cleaned_data['password']
            # the password gets initialized to 
            # password1 in the SIgnUpForm 

            user = authenticate(username = username , password = password)
            login(request , user)

            messages.success(request , "You have successfully registered")

            return redirect('home')
        
        else : 
            form = SignUpForm()
            # taking the SignUpForm and passing it
            return render(request , 'register.html' , {'form' : form})
            # passing the context as the form

    return render(request , 'register.html' , {'form' : form})