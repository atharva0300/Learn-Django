import mysql.connector

# creating a database connection
database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Atharva0300@'
    # the password of mysqlclient that i have set while secure isntallation
    # of mysql for 'root'@'localhost'
)

# prepare a cursor object 
cursorObject = database.cursor()

# create a database 
cursorObject.execute("CREATE DATABASE elderco")

print("All done")