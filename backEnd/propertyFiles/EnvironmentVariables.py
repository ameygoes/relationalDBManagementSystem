# ==============================================================
# ======================= SQL PROPERTIES =======================
# ==============================================================

# CONNECTION PROPERTIES
dbUserName = "rdmsUser"

# tobe Encrypted
password = "gAAAAABhK576ntIFAmqgnXs6u06dtzHoJbPGzXNXTjRIRve-Z9aBF3Ztvtsz3fH6d2_QMtve15emipkg0Q_GcOAnYRMJiNxaUg=="
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

# PII COLUMN NAMES
piiColumns = ["firstname","surname","email","aadhar","PAN","passport","mobileNumber","permanantAddress","residentialAddress"]

# ==============================================================
# =========== ENCRYPTION AND DECRYTION PROPERTIES ==============
# ==============================================================
pathToDecryptionKey = "../SecretFiles/decryptionKey.key"
