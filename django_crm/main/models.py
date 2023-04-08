from django.db import models

# setting the database contents, we define the model here 
# dont't have to define specifically for a database 
# works on all the database like mysql, pstgres , sqlite 
# django will take this and convert this int sql or postgres 

class Record(models.Model) : 
    created_at = models.DateTimeField(auto_now_add = True)
    # date time field 
    # setting the value to the current date and time value 

    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50) 
    phone = models.CharField(max_length = 10)
    address = models.CharField(max_length =100)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50)
    zipcode = models.CharField(max_length = 6)

    def __str__(self) : 
        # invoking the priate str function 
        return (f"{self.first_name} {self.last_name}")
        # returns the above string, if we call this string 
        # ie- while displaying this string on the html form
    



    