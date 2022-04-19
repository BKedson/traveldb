from ast import arg, operator
from msilib.schema import Error
from unittest import result

def executeCommand(command, args):
    if command == "SHOW":
        if len(args) == 0 or args[0] == "STUDENTS":
            getStudentInfo()
        elif args[0] == 'CLUBFUNDS':
            if len(args) >= 2:
                getClubs()
            else:
                print("Specify a dollar amount")
        elif args[0] == 'STUDENTDRIVING':
            if len(args) == 0:
                getStudentsDriving()
    
    else:
        print("*Error*: Unknown/Unsupported command")

@app.route("/getAll")
def getStudentInfo():
    operation = (f"SELECT S.caseID, S.name, AVG(S.year) FROM Student S WHERE S.turnedInPaperwork = true GROUP BY S.caseID")
    try:
        mycursor.execute(operation)
        result = mycursor.fetchall()
        print(result)
    except Error as e:
        print(f"The error '{e}' occured")

def getClubs():
    return 0

def getStudentsDriving():
    return 0


