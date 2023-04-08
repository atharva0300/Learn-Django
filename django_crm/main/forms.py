from django.contrib.auth.forms import UserCreationForm 
# creates users 

from django.contrib.auth.models import User
# for the user model

# importing django forms 
from django import forms

# importing the Record model 
from .models import Record


# class for signup class 
class SignUpForm(UserCreationForm) : 
    # inheriting the UserCreationForm to the class 
    # to make the user form 
    email = forms.EmailField(label = '' , widget = forms.TextInput(attrs = {'class' : 'form-control' , 'placeholder' : 'Email Address'}))
    # label for email is set to nothin - > ''
    # widget says that the form input field is a text box
    # inside the attrs is the attributes to style the form ( html attributes )



    first_name = forms.CharField(label = "" , max_length = 100 , widget = forms.TextInput(attrs = {'class' : 'form-control' , 'placeholder' : 'First Name'})    )
    # the max_length is the max length of the charaters in the input field 


    last_name = forms.CharField(label = "" , max_length = 100 , widget = forms.TextInput(attrs = {'class' : 'form-control' , 'placeholder' : 'Last Name'}))


    class Meta : 
        model  = User
        # model is set to the User model

        fields = ('username' , 'first_name' , 'last_name' , 'email' , 'password1' , 'password2') 
        # the fields in the form -> email ,  first_name , last_name and more 


        def __init__(self, *args, **kwargs):
            super(SignUpForm, self).__init__(*args, **kwargs)
            # the super function, will take the SignUpForm class 
            # it has inherited the class and passes the arguments from that class to here 
            

            self.fields['username'].widget.attrs['class'] = 'form-control'
            self.fields['username'].widget.attrs['placeholder'] = 'User Name'
            self.fields['username'].label = ''
            self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

            self.fields['password1'].widget.attrs['class'] = 'form-control'
            self.fields['password1'].widget.attrs['placeholder'] = 'Password'
            self.fields['password1'].label = ''
            self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

            self.fields['password2'].widget.attrs['class'] = 'form-control'
            self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
            self.fields['password2'].label = ''
            self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	



# creating a form for adding record 
class AddRecordForm(forms.ModelForm) :
    first_name = forms.CharField(max_length=50 , required=True , widget = forms.widgets.TextInput(attrs = {'placeholder' : 'First Name' , 'class' : 'form-control'}) , label = '')
    last_name = forms.CharField(max_length=50 , required=True , widget = forms.widgets.TextInput(attrs = {'placeholder' : 'Last Name' , 'class' : 'form-control'}) , label = '')
    email =forms.CharField(max_length=50 , required=True , widget = forms.widgets.TextInput(attrs = {'placeholder' : 'Email' , 'class' : 'form-control'}) , label = '')
    phone = forms.CharField(max_length=50 , required=True , widget = forms.widgets.TextInput(attrs = {'placeholder' : 'Phone' , 'class' : 'form-control'}) , label = '')
    address = forms.CharField(max_length=100 , required=True , widget = forms.widgets.TextInput(attrs = {'placeholder' : 'Address' , 'class' : 'form-control'}) , label = '')
    city = forms.CharField(max_length=50 , required=True , widget = forms.widgets.TextInput(attrs = {'placeholder' : 'City' , 'class' : 'form-control'}) , label = '')
    state = forms.CharField(max_length=50 , required=True , widget = forms.widgets.TextInput(attrs = {'placeholder' : 'State' , 'class' : 'form-control'}) , label = '')
    zipcode = forms.CharField(max_length=50 , required=True , widget = forms.widgets.TextInput(attrs = {'placeholder' : 'Zipcode' , 'class' : 'form-control'}) , label = '')


    # set up the class of Meta 
    # and designate which model to use 
    class Meta : 
        model = Record

        # designating the field
        exclude = ("user" ,)