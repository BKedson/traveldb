from ast import arg, operator
from msilib.schema import Error
from unittest import result
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="bk",  # the user you set when installing MySQL
    passwd="PurplePlum2!",  # the password you set when installing MySQL
    database="traveldb" # only run this line after running the database creation command below
)
mycursor = db.cursor()

def customQueries(command, args):
    c = command.lower()
    if c == "show":
        if args.lower() == "students":
            getStudentInfo()
            getInput(True)
        elif args.lower() == 'clubs':
            getClubInfo()
            getInput(True)
        elif args.lower() == 'events':
            getEventInfo()
            getInput(True)
        elif args.lower() == 'cars':
            getCarInfo()
            getInput(True)
        else:
            print("*Error*: Invalid table selected")
            getInput(True)
    elif c == "members":
        membersOf(args)
        getInput(True)
    elif c == "afford":
        affordEvent(args)
        getInput(True)
    elif c == "exit":
        print("Exited.")
    elif c == "help":
        main()
    else:
        print("*Error*: Unknown/Unsupported command")
        getInput(True)

def getStudentInfo():
    operation = ("SELECT * FROM Student")
    try:
        mycursor.execute(operation)
        result = mycursor.fetchall()
        print(result)
    except Error as e:
        print("The error '{e}' occured")

def getClubInfo():
    operation = ("SELECT * FROM Club")
    try:
        mycursor.execute(operation)
        result = mycursor.fetchall()
        print(result)
    except Error as e:
        print("The error '{e}' occured")

def getEventInfo():
    operation = ("SELECT * FROM Event")
    try:
        mycursor.execute(operation)
        result = mycursor.fetchall()
        print(result)
    except Error as e:
        print("The error '{e}' occured")

def getCarInfo():
    operation = ("SELECT * FROM carGoes")
    try:
        mycursor.execute(operation)
        result = mycursor.fetchall()
        print(result)
    except Error as e:
        print("The error '{e}' occured")

def affordEvent(event):
    operation = ("SELECT DISTINCT c.name FROM Club c, Event e WHERE c.funds >= e.cost")
    checkOperation = ("SELECT eventName FROM Event")
    try:
        foundEvent = False
        mycursor.execute(checkOperation)
        eventList = mycursor.fetchall()
        for currentEvent in eventList:
            if "('{}',)".format(event) == str(currentEvent):
                mycursor.execute(operation)
                result = mycursor.fetchall()
                print(result)
                foundEvent = True
        if not foundEvent:
            print("*Error*: Bad event name")
    except Error as e:
        print("The error '{e}' occured")

def membersOf(club):
    operation = ("SELECT s.name FROM Student s, Club c, isMember m WHERE s.caseID = m.caseID AND m.clubID = c.clubID AND c.name = \"{}\"".format(club))
    checkOperation = ("SELECT name FROM Club")
    try:
        foundClub = False
        mycursor.execute(checkOperation)
        clubList = mycursor.fetchall()
        for currentClub in clubList:
            if "('{}',)".format(club) == str(currentClub):
                mycursor.execute(operation)
                result = mycursor.fetchall()
                print(result)
                foundClub = True
        if not foundClub:
            print("*Error*: Bad club name")
    except Error as e:
        print("The error '{e}' occured")

def main():
    print("**********************************************************************")
    print("Welcome to the Club Travel Organizer Command Line Interface! Type 'exit' to leave.")
    print("SHOW <Table>: Fetches a table from the database")
    print("MEMBERS <Club Name>: Finds all the members of a given club")
    print("AFFORD <Event Name>: Lists all clubs that can afford a given event")
    print("HELP: See options again")
    print("EXIT: Exit the CLI")
    print("**********************************************************************")
    getInput(True)

def getInput(cont):
    print()
    if cont:
        command = ""
        args = ""
        command = input("Command: ")
        if command.lower() == "show" or command.lower() == "members" or command.lower() == "afford":
            args = input("Arguments: ")
        customQueries(command, args)

if __name__ == "__main__":
    main()
