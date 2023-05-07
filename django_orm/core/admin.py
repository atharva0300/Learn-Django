from django.contrib import admin

# importing models 
from students.models import Student , Teacher

# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)