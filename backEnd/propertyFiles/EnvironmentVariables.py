# ==============================================================
# ======================= SQL PROPERTIES =======================
# ==============================================================

# CONNECTION PROPERTIES
dbUserName = "rdmsUser"
# tobe Encrypted
password = "admin@123"
hostName = "localhost"
portName = "3306"

# TABLE PROPERTIES
dbName = "rdms"
tableName = "studentdetails"
coloumnNames = "rollNumber,registrationId,firstname,surname,fathersName,mothersName,email,isAadhar,aadhar,isPAN,PAN,\
isPassport,passport,isIndian,nationality,mobileNumber,permanantAddress,residentialAddress,tenthCGPA,twelthCGPA,tenthGrade,\
twelthGrade,firstSemCGPA,secondSemCGPA,thirdSemCGPA,fourthSemCGPA,fifthSemCGPA,sixthSemCGPA,seventhSemCGPA,eightthSemGCPA,isDiploma,\
diplomaMarks,isBacklog,numberOfBacklogs,activeBacklog,PassiveBacklog,isYD,YDYears,isEducationGap,educationGapYears,isPICTStudent,currentBatch"

# COMMANDS TOBE EXECUTED
# Command to get Lower Bound
getLowerBound = "SELECT MAX(rollNumber) FROM {}"

# Command to Insert Dummy Data
insertData = "INSERT INTO {} ({}) VALUES {}"

# INSERT DUMMY Data
numberofDummyDataToBeInserted = 1000
