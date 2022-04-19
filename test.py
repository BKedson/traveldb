import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="andrew",
    passwd="carokann47",
    database="testdatabase"
)

mycursor = db.cursor()

print("burgger")
