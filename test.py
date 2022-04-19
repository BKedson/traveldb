from datetime import datetime
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="andrew",  # the user you set when installing MySQL
    passwd="carokann47",  # the password you set when installing MySQL
    database="testdatabase"
)

mycursor = db.cursor()

# this is the code to create and edit a test database

# # creates the database
# mycursor.execute("CREATE DATABASE testdatabase")

# # creates a table in the db
# mycursor.execute(
#     "CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")

# inserts into a table in the db (%s signifies a variable you can set in the tuple that comes after the SQL query (i.e. "tim", 19))
# mycursor.execute("INSERT INTO Person (name, age) VALUES(%s, %s)", ("tim", 19))
# db.commit()  # insertions require a commit to actually change the db

# mycursor.execute(
#     "CREATE TABLE Test (name varchar(50) NOT NULL, created datetime NOT NULL, gender ENUM('M', 'F','O') NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")

# mycursor.execute("INSERT INTO Test (name, created, gender) VALUES (%s, %s, %s)",
#                  ("TIM", datetime.now(), "M"))
# mycursor.execute("INSERT INTO Test (name, created, gender) VALUES (%s, %s, %s)",
#                  ("JOE", datetime.now(), "M"))
# mycursor.execute("INSERT INTO Test (name, created, gender) VALUES (%s, %s, %s)",
#                  ("SAKETH", datetime.now(), "F"))
# db.commit()

# # Describe the Person Table
# mycursor.execute("DESCRIBE Person")

# for x in mycursor:
#     print(x)
