from django.shortcuts import render
from django.db import connection
from django.db.models import Q 

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


def student_list____(request) : 
    posts = Student.objects.filter(Q(surname__startswith = 'abc')| Q(surname__startswith='ma') | Q(surname__startswith='atha'))    # this returns a queryset with where it matches the passed parameter to the value 
    # this is a select from where statement 
    # the | is the OR operator, which sends the value for both the queries and combines them

    print(posts)
    print('\nconnection.queries : ' , connection.queries)

    return render(request , 'output.html' , {'posts' : posts})

def student_list____(request) : 
    posts = Student.objects.filter(classroom = 3) & Student.objects.filter(firstname__startswith = 'ath')
    # AND query -> this query will check for all the conditions 
    
    
    # posts = Student.objects.filter(classroom = 1) & Student.objects.filter(firstname__startswith = 'ath')
    # This will result in no query object because there is no student who starts with 'ath' and in the classroom 1 
    # Both te paramters must be true 
    # TRUE & TRUE & TRUE -> TRUE
    # TRUE & FALSE & TRUE & anything -> FALSE
    
    # posts = Student.objects.filter(Q(classroom = 3) & Q(firstname__startswith = 'ath'))
    # Q query for AND 
    
    print(posts)
    print('\nconnection.queries : ' , connection.queries)

    return render(request , 'output.html' , {'posts' : posts})


def student_list_____(request) : 
    posts = Student.objects.all().values_list("firstname").union(Teacher.objects.all().values_list("firstname"))
    # This query will obtain all the firstnames from the Student table and make a union
    # with all the firstnames from the Teacher Table 

    # values_list is similar to values, just instead of returning a dictionry it returns a tuple when itearted over
    print(posts)
    print('\nconnection.queries : ' , connection.queries)

    return render(request , 'output.html' , {'posts' : posts})


def student_list1(request) : 
    item1 = Student.objects.exclude(age = 13)
    # This is a NOT query 
    # this will show all the records which has age!=13
    # exclude is the keyword used for NOT 

    item2 = Student.objects.exclude(age__gt=12)
    # excludes all the records which has age > 12

    item3 = Student.objects.filter(age__lt=12)
    # gets all the records with the age < 12

    item4 = Student.objects.filter(~Q(age__gt=12))
    # Excludes records with age > 12 

    item5 = Student.objects.filter(~Q(age__gt=12) & Q(firstname__startswith='ta'))
    # filter with ~ Q age > 12 and Q firstname which startswith ta 

    item6 = Student.objects.exclude(age__gte=12)
    # excludes all the records which has age >= 12

    item7 = Student.objects.filter(age__lte=12)
    # gets all the records with the age <= 12
    

    posts = [{
        'exclude' : item1
    },
    {
        'exclude age > 12' : item2
    },
    {
        'filter age < 12' : item3
    },
    {
        'filter with ~Q age > 12' : item4 
    },
    {
        'filter with ~ Q age > 12 and Q firstname which startswith ta ' : item5
    },
    {
        'exclude age >= 12 ' : item6
    },
    {
        'filter age <= 12' : item7
    }
    ]

    # values_list is similar to values, just instead of returning a dictionry it returns a tuple when itearted over
    print(posts)
    print('\nconnection.queries : ' , connection.queries)

    return render(request , 'output.html' , {'posts' : posts})



def student_list2(request) : 
   
    item1 = Student.objects.filter(classroom = 2).only('firstname' , 'age')
    # obtain all the records with classroom=2 and get their firstnames and age only 
    
    item2 = Student.objects.raw("SELECT * FROM students_student")
    # raw() allows you to make SQL queries directly 

    for p in Student.objects.raw("SELECT * FROM students_student") : 
        print("p : " , p)

    
    print('\nAnother raw query \n')
    item2 = Student.objects.raw("SELECT * FROM students_student WHERE age=12")
    # raw() allows you to make SQL queries directly 

    for p in Student.objects.raw("SELECT * FROM students_student") : 
        print("p : " , p)

    """
    Deferred model fields 

    for p in Person.objects.raw("SELECT id, first_name FROM myapp_person"):
     print(
         p.first_name,  # This will be retrieved by the original query
         p.last_name,  # This will be retrieved on demand
    )
    
    """

    posts = [
        {
            'obtain all the records with classroom=2 and get their firstnames and age only ' : item1,
            'data' : {
                'firsname' : item1[0].firstname,
                'surname' : item1[0].surname,
                'age' : item1[0].age,
                'classroom' : item1[0].classroom
            }
        },
        {
            'info on the above query output ' : 'The only() takes the Query object ( everything ) but, surname and classroom can also be accessed, this is because, with only() we are collecting only the firstname and the age, which gives the permance boost as we are not storing other column data, when we access it, django then accesses them from the database, so it makes an additional query.'
        },
        {
            'raw' : item2
        }
    ]

    # values_list is similar to values, just instead of returning a dictionry it returns a tuple when itearted over
    print(posts)
    print('\nconnection.queries : ' , connection.queries)

    return render(request , 'output.html' , {'posts' : posts})


def dictfetchall(cursor) : 
    # takes the SQL output and converts it into Python dictionary
    desc = cursor.description
    return[
        dict(zip([col[0] for col in desc] , row ))
        for row in cursor.fetchall()
    ]


def student_list3(request) :
    # bringing the cursor 
    cursor = connection.cursor()    # obtaining the cursor from connection
    cursor.execute("SELECT count(*) FROM students_student")      # the query to be executed
    r = cursor.fetchone()   # fetched one value 
    # This code is bypassing the ORM and performing SQL directly 

    cursor = connection.cursor()    # obtaining the cursor from connection
    cursor.execute("SELECT * FROM students_student")      # the query to be executed

    r2 = cursor.fetchall()
    
    cursor = connection.cursor()    # obtaining the cursor from connection
    cursor.execute("SELECT * FROM students_student")      # the query to be executed

    r3 = dictfetchall(cursor)

    for i in r3 : 
        print(i)

    print("r : " , r)

    posts = [{
        'r ' : r
    },
    {
        'r fetchall()' : r2
    },
    {
        'f2 dict fetch all function ' : r3
    }
    ]
    print(posts)
 
    # print(posts.query)  # the actual SQL query which was used to perform the operations 

    print('cononection.queries : ' , connection.queries)   # actual SQL query with the amount of time it took to execute the code


    return render(request , 'output.html' , {'posts' : posts})



def student_list(request) :


    posts = []
    print(posts)
 
    # print(posts.query)  # the actual SQL query which was used to perform the operations 

    print('cononection.queries : ' , connection.queries)   # actual SQL query with the amount of time it took to execute the code


    return render(request , 'output.html' , {'posts' : posts})
