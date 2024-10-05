import mysql.connector
from decouple import config

dataBase = mysql.connector.connect(
    host = config('DB_HOST'),
    user = config('DB_USER'),
    passwd = config('DB_PASSWORD')
)

# prepare a cursor object
cursorObject = dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE db")
print("All Done!")