# Importing Builtin Libraries
import sys
sys.path.append("../propertyFiles")
sys.path.append("../SQLConnectors")
import string
import random

# Importing User defined Modules
from sqlConnector import *
from EnvironmentVariables import *
from dummyDataPayload import *

# COMMAND TO GET LOWERBOUND
getLowerBoundCmd = getLowerBound.format(tableName)

# GET LOWERBOUND
maxValueInDB = executeGetCommand(getLowerBoundCmd)

# RETURNS A TUPLE - GET FIRST ELEMENT
lowerBound = maxValueInDB[0] + 1
upperBound = lowerBound + numberofDummyDataToBeInserted

# number of characters in the PrefixEmail string.
maxLengthOfPrefixEmail = 9

# Get command Executed
commandString = ""
templateString = "{}"
comma = ","

# RUN FOR LOOP TO GENERATE DUMMY DATA
for dynamicNumber in range (lowerBound, upperBound):

    # CREATE RANDOM ALPHANUMERIC EMAIL FOR INSERTION
    alphaNumericEmail = ''.join(random.choices(string.ascii_uppercase + string.digits, k = maxLengthOfPrefixEmail))

    templateString = """({},"{}","{}","{}","{}","{}","{}",{},{},{},"{}",{},"{}",{},"{}",{},"{}","{}",{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})"""
    commandString = commandString + templateString.format(int(rollNumber.format(dynamicNumber)),registrationId.format(dynamicNumber),firstname.format(dynamicNumber),surname.format(dynamicNumber),
                                                          fathersName.format(dynamicNumber),mothersName.format(dynamicNumber),email.format(alphaNumericEmail),isAadhar,aadhar.format(dynamicNumber),
                                                          isPAN,PAN.format(dynamicNumber),isPassport,passport.format(dynamicNumber),isIndian,nationality,int(mobileNumber.format(dynamicNumber)),
                                                          permanantAddress.format(dynamicNumber),residentialAddress.format(dynamicNumber),tenthCGPA,twelthCGPA,tenthGrade,twelthGrade,firstSemCGPA,secondSemCGPA,
                                                          thirdSemCGPA,fourthSemCGPA,fifthSemCGPA,sixthSemCGPA,seventhSemCGPA,eightthSemGCPA,isDiploma,diplomaMarks,isBacklog,numberOfBacklogs,activeBacklog,
                                                          PassiveBacklog,isYD,YDYears,isEducationGap,educationGapYears,isPICTStudent,currentBatch)
    # ADD COMMA AFTER EVERY ROW BUT LAST ONE
    if(dynamicNumber<upperBound-1):
        commandString = commandString + ","


# Execute Command to Insert Values
result = executeInsertCommand(insertData.format(tableName,coloumnNames,commandString))

# Sample of Rows inserted
print("Total rows inserted {}".format(numberofDummyDataToBeInserted))
