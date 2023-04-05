from django.contrib import admin

from .models import Question, Choice

#admin.site.register(Question)

# customizing the admin form here 


class ChoiceInline(admin.StackedInline) : 
    model = Choice
    extra = 3 


class QuestionAdmin(admin.ModelAdmin) :
    # fields = ['pub_date'  , 'question_text']

    # using fieldsets 
    fieldsets = [
        (None , {"fields" : ["question_text"]}),
        ("Date information" , {"fields" : ["pub_date"]}),
    ]

    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]

    list_filter = ["pub_date"]
    # for filtering the pub_date

    search_fields = ["question_text"]
    # for searching the question text

    




# class ChoiceInline(admin.TabularInline) : 


admin.site.register(Question , QuestionAdmin)
#admin.site.register(Choice, ChoiceInline)