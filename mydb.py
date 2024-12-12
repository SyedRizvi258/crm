import psycopg2
from decouple import config

# Connect to PostgreSQL
dataBase = psycopg2.connect(
    host=config('DB_HOST'),
    user=config('DB_USER'),
    password=config('DB_PASSWORD')
)

# Create a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE db")

# Commit the changes
dataBase.commit()

print("Database created successfully!")

# Close the cursor and connection
cursorObject.close()
dataBase.close()