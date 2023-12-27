import mysql.connector

database = mysql.connector.connect(
   host = "localhost",
   user = "root",
   passwd = "9064871878Dm@"

)

#prepare a cursor object

cursorObject = database.cursor()

#create a database
cursorObject.execute("CREATE DATABASE CollabCo")

print("All Done!")