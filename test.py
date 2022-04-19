from datetime import datetime
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="<your username here>",  # the user you set when installing MySQL
    passwd="<your password here>"  # ,  # the password you set when installing MySQL
    # database="traveldb" # only run this line after running the database creation command below
)

mycursor = db.cursor()

# this is the code to create and edit a test database

# # creates the database
# mycursor.execute("CREATE DATABASE traveldb")

# creates a table in the db

# creates the Student table
# mycursor.execute(
#     "CREATE TABLE Student (caseID VARCHAR(6) PRIMARY KEY, name VARCHAR(50), year int UNSIGNED, address VARCHAR(100), phone varchar(50), email varchar(50), turnedInPaperwork BOOLEAN)")

# # creates the Event table
# mycursor.execute(
#     "CREATE TABLE Event (eventID int PRIMARY KEY AUTO_INCREMENT, eventName VARCHAR(50), eventLocation VARCHAR(100), startDate DATE, endDate DATE, capacity int, cost float)")

# # creates the Club table
# mycursor.execute(
#     "CREATE TABLE Club (clubID int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), funds float, presID int, sponsorName VARCHAR(50))")

# # creates the carGoes table
# mycursor.execute(
#     "CREATE TABLE carGoes (plateNum VARCHAR(10) PRIMARY KEY, make VARCHAR(25), model VARCHAR(50), capacity int, eventID int, FOREIGN KEY (eventID) REFERENCES Event(eventID))")

# # creates the isDriver table
# mycursor.execute(
#     "CREATE TABLE isDriver (caseID VARCHAR(6), plateNum VARCHAR(10), eventID int, FOREIGN KEY (eventID) REFERENCES Event(eventID), FOREIGN KEY (caseID) REFERENCES Student(caseID), FOREIGN KEY (plateNum) REFERENCES carGoes(plateNum))")

# # creates the isOwner table
# mycursor.execute(
#     "CREATE TABLE isOwner (caseID VARCHAR(6), plateNum VARCHAR(10), eventID int, FOREIGN KEY (eventID) REFERENCES Event(eventID), FOREIGN KEY (caseID) REFERENCES Student(caseID), FOREIGN KEY (plateNum) REFERENCES carGoes(plateNum))")

# # creates the isRiding table
# mycursor.execute(
#     "CREATE TABLE isRiding (caseID VARCHAR(6), plateNum VARCHAR(10), eventID int, FOREIGN KEY (eventID) REFERENCES Event(eventID), FOREIGN KEY (caseID) REFERENCES Student(caseID), FOREIGN KEY (plateNum) REFERENCES carGoes(plateNum))")

# # creates the isGoing table
# mycursor.execute(
#     "CREATE TABLE isGoing (caseID VARCHAR(6), eventID int, FOREIGN KEY (caseID) REFERENCES Student(caseID), FOREIGN KEY (eventID) REFERENCES Event(eventID))")

# # creates the isParticipating table
# mycursor.execute(
#     "CREATE TABLE isParticipating (caseID VARCHAR(6), eventID int, FOREIGN KEY (caseID) REFERENCES Student(caseID), FOREIGN KEY (eventID) REFERENCES Event(eventID))")

# # creates the isMember table
# mycursor.execute(
#     "CREATE TABLE isMember (caseID VARCHAR(6), clubID int, FOREIGN KEY (caseID) REFERENCES Student(caseID), FOREIGN KEY (clubID) REFERENCES Club(clubID))")


# #inserts into a table in the db (%s signifies a variable you can set in the tuple that comes after the SQL query (i.e. "tim", 19))
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
