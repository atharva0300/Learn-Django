from django.shortcuts import render, redirect

# importing django authentication 
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages

from django.http import HttpResponse

# importing the form 
from .forms import SignUpForm

# importing the Records model
from .models import Record

from .forms import AddRecordForm



# Create your views here.
def home(request) : 

    records = Record.objects.all()
    # getting all the data from the Record

    # if the user is not POSTing, then the 
    # user is logged in 
    # and we want to display the data 



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

    else : 
        return render(request , 'home.html' , {'records' : records})

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


def customer_record(request , pk ) : 
    # the primary key will be taken from the url
    if request.user.is_authenticated : 
        # cehecking if the user is authenticated or not 
        # request.user gives the user 


        # let us look up that record
        customer_record = Record.objects.get(id = pk)
        # getting the record which has the pk mentioned 

        return render(request , 'record.html' , {'customer_record' : customer_record})

    else : 
        # if the user is not authenticated 
        messages.success(request , "You must be logged in to view that page")
        return redirect('home')



def delete_record(request , pk) :
    # deleting the record

    if request.user.is_authenticated : 

        deleteit = Record.objects.get(id = pk)
        # get the record with the pk

        deleteit.delete()
        # deletes the record from the database

        messages.success(request , "Record deleted successfully")

        return redirect('home')

    else: 
        # if the user is not logged in 
        # then
        messages.success(request , "You cannot delete the record as you are not logged in")

        return redirect('home')
    

def add_record(request) : 
    # check if the user is authenticated 
    if request.user.is_authenticated : 

        form = AddRecordForm(request.POST or None)
        
        if request.method == 'POST' : 
            # is the form valid ? 
            if form.is_valid() : 
                add_record = form.save()

                messages.success(request , "Record Added...")
                return redirect('home')

        else : 

            return render(request , 'add_record.html' , {'form' : form})
    
    else : 

        # if not authenticated 
        messages.success(request , "You must be loggedin")
        return redirect('home')
    


def update_record(request , pk) :
    # updating the record

    if request.user.is_authenticated : 

        current_record = Record.objects.get(id = pk)
        # getting the data of the pk record from the database

        # populating the form with the data taken from the database 
        # we initializer the instance to current_record
        form =  AddRecordForm(request.POST or None , instance = current_record)

        if form.is_valid() : 
            # if they have posted 

            form.save()
            # save the form

            messages.success(request , "Record has been updated")
            return redirect('home')

        return render(request , 'update_record.html' , {'form' : form})
    
    else : 
        # if not authenticated
        messages.success(request , "You must be loggedin")
        return redirect('home')