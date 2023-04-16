from django.forms import ModelForm
from django import forms

# importing the model 
from .models import formModel

CHOICES = [
    ('1' , 'First'),
    ('2' , 'Second')
]

# creaing a form 
class myForm(ModelForm) : 
    name = forms.CharField(
        label = "Name", max_length= 20, required=False,
        widget = forms.TextInput(attrs = {
            'placeholder' : 'Enter Name',
            'style' : 'color : blue;',
            'class' : 'form-control'
        })
        )
    address = forms.Textarea()
    choice = forms.ChoiceField(
        widget=forms.RadioSelect(
        attrs = {
        'class' : 'form-control'
        }
        ) , choices = CHOICES,
        
    )
    url = forms.URLField(required=False)
    uuid = forms.UUIDField(required=False)
    floating = forms.FloatField(required=False)
    number = forms.DecimalField(required=False)
    checkbox = forms.ChoiceField(
        widget=forms.CheckboxSelectMultiple(
        attrs = {
        'class' : 'form-control'
        }
        ) , choices=CHOICES
    )
    file = forms.FileField(max_length=12 ,  required=False , widget = forms.FileInput(
        attrs = {
        'class' : 'form-control'
        }
    ))
    email = forms.EmailField(required=False , widget = forms.EmailInput(
        attrs = {
        'class' : 'form-control'
        }
    ))
    cc_myself = forms.BooleanField(required=False)


    class Meta : 
        model = formModel

        fields = [
            'name',
            'address'
        ]