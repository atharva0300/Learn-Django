from django.db import models
from django.utils import timezone
import datetime
from django.contrib import admin


class Question(models.Model) : 
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField("date published")
    


    
    @admin.display(
        boolean = True,
        ordering = 'pub_date',
        description = 'Published recently?'
    )
    def was_published_recently(self) : 
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model) : 
    question = models.ForeignKey(Question , on_delete = models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default = 0)


# the Field class inside the models.Field, tells us what kind of data it holds. Ex- CharField, IntegerField, FloatField etc
# the fields have different parameters depending on the type of the field
# Django supports all the common database relationships: many-to-one, many-to-many, and one-to-one.

# After creating the model, we need to create a Python-database API for accessing the Question and the Choice from the models.py 
# add polls.apps.PollsConfig in the installed_apps , this does the above work