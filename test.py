from datetime import datetime
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="bk",  # the user you set when installing MySQL
    passwd="PurplePlum2!",  # the password you set when installing MySQL
    database="traveldb" # only run this line after running the database creation command below
)

mycursor = db.cursor()

# this is the code to create and edit a test database
# # creates the database
# mycursor.execute(
# "CREATE DATABASE traveldb")

# this is the sample data for the Student table
# mycursor.execute(
# "INSERT INTO Student(caseID,name,year,address,phone,email) VALUES('gwk12','Ginger Mckay',1,'952-112 Volutpat Road','(336) 254-6125','ac.ipsum@yahoo.net'),('lzp22','Lyle Padilla',2,'Ap #881-4919 Vivamus Street','(947) 361-7372','elit@aol.ca'),('hlh333','Halee Holt',3,'903-1257 Luctus Rd.','(321) 660-3525','massa.vestibulum@yahoo.com'),('cpr45','Charissa Randall',4,'Ap #484-9603 Ornare. St.','(648) 905-3225','vitae.erat.vel@aol.net'),('dos521','Diana Suarez',5,'P.O. Box 374, 9001 Luctus Rd.','(320) 345-6711','dignissim.lacus.aliquam@aol.com'),('bkm691','Bert Mayer',1,'P.O. Box 532, 316 Et St.','1-339-324-3860','justo@protonmail.com'),('mdf7','Maris Frederick',2,'Ap #281-1372 Et Road','1-898-937-8067','nullam.velit@outlook.edu'),('zym89','Zachary Malone',3,'773-2239 Duis Ave','(853) 894-5703','sapien@aol.net'),('quw91','Quyn Walters',4,'Ap #272-4995 Proin Street','1-978-224-4974','eu@hotmail.org'),('qok10','Quentin Kline',5,'Ap #721-9119 Nibh Ave','1-275-895-6527','nec@icloud.com'),('waa113','Warren Adkins',1,'Ap #232-1184 Ac Street','(601) 361-3574','ac.ipsum@google.net'),('mcs101','Merritt Santiago',2,'438 Mus. St.','(235) 787-7831','nunc.ullamcorper@google.ca'),('aoh131','Alexis Hinton',3,'Ap #727-111 Id, Rd.','(453) 231-4875','condimentum@outlook.org'),('sph147','Sybil Holder',4,'P.O. Box 268, 1499 Cursus Av.','(132) 813-8282','tristique.pharetra@hotmail.org'),('oir159','Odysseus Rosa',5,'170-223 Nulla. Rd.','1-371-673-5462','ultrices.vivamus.rhoncus@yahoo.ca');")

# this is the sample data for the event table
# mycursor.execute(
# "INSERT INTO Event(eventID,eventName,eventLocation,startDate,endDate,capacity,cost)VALUES(1,'Cleveland Open','Ap #446-825 Aliquam Street','2022-04-03','2022-04-03',13,'1030.31'),(2,'Hack Cleveland','Ap #963-7391 Sit Road','2022-09-05','2022-09-07',1,'387.91'),(3,'Celebrate Cleveland','173-5666 Luctus St.','2022-05-20','2022-05-22',4,'0.00'),(4,'Expensive Concert','599-9466 Arcu. Av.','2023-08-25','2023-08-25',17,'9980.96'),(5,'Intercollegiate Quiz Bowl','Ap #497-3892 Volutpat Street','2022-12-14','2022-12-15',11,'126.32');")

# this is the sample data for the club table
# mycursor.execute(
# "INSERT INTO Club(clubID,name,funds,presID,sponsorName)VALUES(1,'Chess Club','2000.52','gwk12','Meghan Delacruz'),(2,'Quiz Bowl','14.50','gwk12','Olympia Dillon'),(3,'Hacker Society','367.85','hlh333','Ima Hull'),(4,'Rich Club','3777.00','dos521','Inga Massey');")

# this is the sample data for the carGoes weak entity table
# mycursor.execute(
# "INSERT INTO carGoes(plateNum,make,model,capacity,eventID)VALUES('PCM12KG','Toyota','Camry',3,5),('JLH33UN','Ford','F150',4,1),('NNR30SG','Ford','Model T',4,4),('KWS11LY','Toyota','Camry',1,5),('TVX38XY','Nissan','Altima',3,4);")

# creates the sample data for the isDriver table
# mycursor.execute(
# "INSERT INTO isDriver VALUES('hlh333','PCM12KG',5),('gwk12','JLH33UN',1),('dos521', 'NNR30SG',4),('zym89', 'KWS11LY',5),('mcs101', 'TVX38XY', 4);")

# creates the sample data for the isOwner table
# mycursor.execute(
# "INSERT INTO isOwner VALUES('hlh333','PCM12KG',5),('gwk12','JLH33UN',1),('dos521', 'NNR30SG',4),('zym89', 'KWS11LY',5),('dos521', 'TVX38XY', 4);")

# creates the sample data for the isRiding table
# mycursor.execute(
# "INSERT INTO isRiding VALUES('hlh333','PCM12KG',5), ('cpr45','PCM12KG',5), ('qok10','PCM12KG',5), ('gwk12','JLH33UN',1), ('bkm691','JLH33UN',1), ('waa113','JLH33UN',1), ('aoh131','JLH33UN',1), ('dos521', 'NNR30SG',4), ('mdf7', 'NNR30SG',4), ('zym89', 'KWS11LY',5),('mcs101', 'TVX38XY', 4), ('sph147', 'TVX38XY', 4);")

# creates the sample data for the isGoing table
# mycursor.execute(
#     "INSERT INTO isGoing VALUES('gwk12',1,0), ('gwk12',5,1),('lzp22',3,0),('hlh333', 3,0),('cpr45',5,1),('dos521',4,1),('bkm691',1,0),('mdf7',4,0),('zym89',5,1),('quw91',3,0),('qok10',5,1),('waa113',1,0),('mcs101',4,0),('aoh131',1,1),('sph147',4,1),('oir159',3,1);")

# creates the sample data for the isParticipating table
# mycursor.execute(
#     "INSERT INTO isParticipating VALUES('gwk12',1), ('gwk12',5),('lzp22',3),('hlh333', 3),('dos521',4),('bkm691',1),('mdf7',4),('quw91',3),('waa113',1),('mcs101',4),('aoh131',1),('sph147',4),('oir159',3);")

# creates the sample data for the isMember table
# mycursor.execute(
#     "INSERT INTO isMember VALUES('gwk12',1), ('gwk12',2),('lzp22',3),('hlh333', 3),('cpr45',2),('dos521',4),('bkm691',1),('mdf7',4),('zym89',2),('quw91',3),('qok10',2),('waa113',1),('mcs101',4),('aoh131',1),('sph147',4),('oir159',3);")


# creates a table in the db

# # creates the Student table
# mycursor.execute(
#      "CREATE TABLE Student (caseID VARCHAR(6) PRIMARY KEY, name VARCHAR(50), year int UNSIGNED, address VARCHAR(100), phone varchar(50), email varchar(50))")

# # # creates the Event table
# mycursor.execute(
#      "CREATE TABLE Event (eventID int PRIMARY KEY AUTO_INCREMENT, eventName VARCHAR(50), eventLocation VARCHAR(100), startDate DATE, endDate DATE, capacity int, cost float)")

# # # creates the Club table
# mycursor.execute(
#     "CREATE TABLE Club (clubID int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), funds float, presID VARCHAR(6), sponsorName VARCHAR(50))")

# # # creates the carGoes table
# mycursor.execute(
#      "CREATE TABLE carGoes (plateNum VARCHAR(10) PRIMARY KEY, make VARCHAR(25), model VARCHAR(50), capacity int, eventID int, FOREIGN KEY (eventID) REFERENCES Event(eventID))")

# # # creates the isDriver table
# mycursor.execute(
#      "CREATE TABLE isDriver (caseID VARCHAR(6), plateNum VARCHAR(10), eventID int, FOREIGN KEY (eventID) REFERENCES Event(eventID), FOREIGN KEY (caseID) REFERENCES Student(caseID), FOREIGN KEY (plateNum) REFERENCES carGoes(plateNum))")

# # # creates the isOwner table
# mycursor.execute(
#      "CREATE TABLE isOwner (caseID VARCHAR(6), plateNum VARCHAR(10), eventID int, FOREIGN KEY (eventID) REFERENCES Event(eventID), FOREIGN KEY (caseID) REFERENCES Student(caseID), FOREIGN KEY (plateNum) REFERENCES carGoes(plateNum))")

# # # creates the isRiding table
# mycursor.execute(
#      "CREATE TABLE isRiding (caseID VARCHAR(6), plateNum VARCHAR(10), eventID int, FOREIGN KEY (eventID) REFERENCES Event(eventID), FOREIGN KEY (caseID) REFERENCES Student(caseID), FOREIGN KEY (plateNum) REFERENCES carGoes(plateNum))")

# # # creates the isGoing table
# mycursor.execute(
#      "CREATE TABLE isGoing (caseID VARCHAR(6), eventID int, turnedInPaperwork BOOLEAN, FOREIGN KEY (caseID) REFERENCES Student(caseID), FOREIGN KEY (eventID) REFERENCES Event(eventID))")

# # # creates the isParticipating table
# mycursor.execute(
#      "CREATE TABLE isParticipating (caseID VARCHAR(6), eventID int, FOREIGN KEY (caseID) REFERENCES Student(caseID), FOREIGN KEY (eventID) REFERENCES Event(eventID))")

# # # creates the isMember table
# mycursor.execute(
#      "CREATE TABLE isMember (caseID VARCHAR(6), clubID int, FOREIGN KEY (caseID) REFERENCES Student(caseID), FOREIGN KEY (clubID) REFERENCES Club(clubID))")


# #inserts into a table in the db (%s signifies a variable you can set in the tuple that comes after the SQL query (i.e. "tim", 19))
# mycursor.execute("INSERT INTO Person (name, age) VALUES(%s, %s)", ("tim", 19))
db.commit()  # insertions require a commit to actually change the db

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
