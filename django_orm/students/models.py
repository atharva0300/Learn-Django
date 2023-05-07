from django.db import models

# Create your models here.
class Teacher(models.Model ): 
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __str__(self)  : 
        return self.firstname


class Student(models.Model) : 
    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    age = models.IntegerField()
    classroom = models.IntegerField()
    teacher = models.CharField(max_length=100)

    def __str__(self) : 
        return self.firstname 
    

"""
DJANGO INTERITANCE OPTIONS 
    1. Abstract models 
    2. Multi-table mdoel inheritance 
    3. Proxy models 
"""

"""
1. Abstract models (Abstract base class - ABC )
Used :  
    1. when you have common information needed for number of other models 
ABC : 
    does not get created
    1. Fields added to other child classes (models)

"""
class BaseItem(models.Model) : 
    title = models.CharField( max_length=50)
    created = models.DateTimeField(auto_now_add=True )
    updated = models.DateTimeField(auto_now=True)

    class Meta : 
        abstract = True # stating this class as an abstract class 
        ordering = ['title'] 

class ItemA(BaseItem) : 
    content = models.TextField()

    class Meta(BaseItem.Meta) : 
        # inheriting the meta class of the parent BaseItem class 
        # we are now accessing the fields of the BaseItem class 
        # we are overriding the ordering field of the BaseItem Abstract class 
        ordering = ['-created'] # ordering by the date of creation


class ItemB(BaseItem) :
    file = models.FileField(upload_to="files")

class ItemC(BaseItem) : 
    file = models.FileField(upload_to="images")

class  ItemD(BaseItem) : 
    slug = models.SlugField(max_length=255 , unique=True)


"""
Multi-table model inheritance
Differences : 
    1. Every model is a model all by itself 
    2. One-to-One link is created automatically 

"""
class Books(models.Model) : 
    title = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)


class ISBN(Books) : 
    # ingeriting the Books table 
    # the books__ptr_id value will be created autometically 

    ISBN = models.TextField()

    # one to one field ( our own custom field )
    books_ptr = models.OneToOneField(
        Books , on_delete=models.CASCADE,  # the other table with which we want to make the relationship with 
        parent_link = True,
        primary_key= True   # generating primary keys set to True
    )


"""
Proxy Models 

Used : 
    1. Change the behavior of the model 
    2. Proxy models operate on the original model
    3. Can create additional behaviour for the original model
"""

from django.utils import timezone

class BookContent(models.Model) : 
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

class BookOrders(BookContent) : 

    class Meta : 
        proxy = True    # stating this table ( model ) as a proxy model 
        ordering = ['-created']
    
    def created_on(self) : 
        return timezone.now() - self.created