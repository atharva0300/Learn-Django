from django.shortcuts import render

# importing http response 
from django.http import HttpResponse
# the httpResponse, sends the Http response from the django server to the client 
# the response is written in the views.py file 

# importing the Question model 
from .models import Question, Choice
from django.template import loader
# the loader will help render the html file from the template

from django.shortcuts import render

# importing a 404error
from django.http import Http404

# It’s a very common idiom to use get() and raise Http404 if the object doesn’t exist. 
# Django provides a shortcut. Here’s the detail() view, rewritten:
from django.shortcuts import get_object_or_404

from django.http import HttpResponseRedirect

from django.urls import reverse
from django.utils import timezone

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
    question = get_object_or_404(Question , pk = question_id)
    return render(request , "polls/results.html" , {"question" : question})

def vote(request , question_id) : 
    question = get_object_or_404(Question , pk = question_id)
    # this means get the Question whoose primary key is question_id 

    try : 
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    
    except (KeyError , Choice.DoesNotExist) :
        # ( type of the error , boolean value )
        return render(
            request , 
            "polls/detail.html",
            {
                "question" : question,
                "error_message" : "You didn't select a choice"
            }
        )
    
    else: 
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.

        #After incrementing the choice count, the code returns an HttpResponseRedirect rather than a normal HttpResponse. 
        # HttpResponseRedirect takes a single argument: the URL to which the user will be redirected (see the following point for 
        # how we construct the URL in this case).

        return HttpResponseRedirect(reverse("polls:result" , args = (question.id,)))

        # We are using the reverse() function in the HttpResponseRedirect constructor in this example. 
        # This function helps avoid having to hardcode a URL in the view function. 
        # this reverse() call will return a string like

        # "/polls/3/results/"

        # where the 3 is the value of question.id. This redirected URL will then call the 'results' view to display the final page.
    


# problem with hard-coding views 
# There’s a problem here, though: the page’s design is hard-coded in the view. 
# If you want to change the way the page looks, you’ll have to edit this Python code. 
# So let’s use Django’s template system to separate the design from Python by creating a template that the view can use.


from django.views import generic

# writing the view in the form of class instead of function 
class IndexView(generic.ListView) : 
    # using inheritance to pass the ListView child class as a parameter to the IndexView 
    # this is inheritance 
    template_name = 'polls/index.html'
    context_object_name = "latest_question_list"

    def get_queryset(self) : 
        """
    Return the last five published questions (not including those set to be
    published in the future).
    """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
        :5
        ]


class DetailView(generic.DetailView) : 
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self) :
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView) : 
    model = Question
    template_name = "polls/results.html"


"""
We’re using two generic views here: ListView and DetailView. Respectively, those two views abstract the concepts of “display a list of objects” and “display a detail page for a particular type of object.”

    Each generic view needs to know what model it will be acting upon. This is provided using the model attribute.
    The DetailView generic view expects the primary key value captured from the URL to be called "pk", so we’ve changed question_id to pk for the generic views.

By default, the DetailView generic view uses a template called <app name>/<model name>_detail.html. In our case, it would use the template "polls/question_detail.html". The template_name attribute is used to tell Django to use a specific template name instead of the autogenerated default template name. We also specify the template_name for the results list view – this ensures that the results view and the detail view have a different appearance when rendered, even though they’re both a DetailView behind the scenes.

Similarly, the ListView generic view uses a default template called <app name>/<model name>_list.html; we use template_name to tell ListView to use our existing "polls/index.html" template.
"""


def login(request) : 
    return render(request , 'polls/login.html')