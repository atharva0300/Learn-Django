from django.shortcuts import render

# importing http response 
from django.http import HttpResponse
# the httpResponse, sends the Http response from the django server to the client 
# the response is written in the views.py file 

# importing the Question model 
from .models import Question
from django.template import loader
# the loader will help render the html file from the template

from django.shortcuts import render

# importing a 404error
from django.http import Http404

# It’s a very common idiom to use get() and raise Http404 if the object doesn’t exist. 
# Django provides a shortcut. Here’s the detail() view, rewritten:
from django.shortcuts import get_object_or_404


def index(request) :
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list'  : latest_question_list
    }
    return render(request , "polls/index.html" , context)
    # the render, has 3 parameters 
    # 1. the request, which the server has received from the client
    # 2. the path to the html file which it will render
    # 3. the data which it will pass to the html file ( the data is in the form of object )

    #That code loads the template called polls/index.html and passes it a context. 
    # The context is a dictionary mapping template variable names to Python objects.




def detail(request , question_id) : 
    try: 
        question =  Question.objects.get(pk = question_id)
    except Question.DoesNotExist : 
        # raising teh exception that no value is returned to the question variable 
        raise Http404("Question does not exist")
        # returning a 404 error in case of an exception

    
    # using get_object_or_404
    # question = get_object_or_404(Question , pk = question_id)
    # return render(request , "polls/detail.html" , {"question" : question})

    # Why do we use a helper function get_object_or_404() instead of automatically catching the ObjectDoesNotExist exceptions at a higher level, or having the model API raise Http404 instead of ObjectDoesNotExist?

    # Because that would couple the model layer to the view layer. One of the foremost design goals of Django is to maintain loose coupling. Some controlled coupling is introduced in the django.shortcuts module.

    
    # otherwise 
    return render(request , "polls/detail.html" , {"question" : question})


def result(request , question_id) :
    return HttpResponse("You're looking at the result of %s" %question_id)

def vote(request , question_id) : 
    return HttpResponse("You're voting on the question is %s" %question_id)


# problem with hard-coding views 
# There’s a problem here, though: the page’s design is hard-coded in the view. 
# If you want to change the way the page looks, you’ll have to edit this Python code. 
# So let’s use Django’s template system to separate the design from Python by creating a template that the view can use.