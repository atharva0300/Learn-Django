from django.shortcuts import render
from django.db import connection

# importign models 
from .models import Student , Teacher

# Create your views here.
def student_list_(request) :
    posts = Student.objects.all()   # obtaining all the records from the Student table 

    print(posts)
 
    print(posts.query)  # the actual SQL query which was used to perform the operations 

    print('cononection.queries : ' , connection.queries)   # actual SQL query with the amount of time it took to execute the code


    return render(request , 'output.html' , {'posts' : posts})


def student_list__(request) : 
    posts = Student.objects.filter(surname__startswith = 'abc') | Student.objects.filter(surname__startswith='ma')   # this returns a queryset with where it matches the passed parameter to the value 
    # this is a select from where statement 
    # the | is the OR operator, which sends the value for both the queries and combines them

    print(posts)
    print('\nconnection.queries : ' , connection.queries)

    return render(request , 'output.html' , {'posts' : posts})


def student_list(request) : 
    posts = Student.objects.filter(Q(surname__startswith = 'abc')| Q(surname__startswith='ma') | Q(surname__startswith='atha'))    # this returns a queryset with where it matches the passed parameter to the value 
    # this is a select from where statement 
    # the | is the OR operator, which sends the value for both the queries and combines them

    print(posts)
    print('\nconnection.queries : ' , connection.queries)

    return render(request , 'output.html' , {'posts' : posts})

