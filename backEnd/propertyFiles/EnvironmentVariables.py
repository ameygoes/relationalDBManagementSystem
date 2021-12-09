# ==============================================================
# ======================= USER IMPORTS =========================
# ==============================================================
from backEnd.propertyFiles.propertiesUtils import getBaseDir

# ==============================================================
# ========================== BASE DIR ==========================
# ==============================================================
BASE_DIR = getBaseDir()

# ==============================================================
# ======================= SQL PROPERTIES =======================
# ==============================================================

# CONNECTION PROPERTIES
DB_USER_NAME = "rdmsUser"
# password = "gAAAAABhK7M5eUiWIJw4mPdQUWeTo1AshWyTRI6gJ-THPlTuPYYhHMnY1Llrb0gKZ9ZN0bpAkNvXeWezPLnYR2B1fBUu5FwKZg==" --rootPaass
# PASSWORD = "gAAAAABhK576ntIFAmqgnXs6u06dtzHoJbPGzXNXTjRIRve-Z9aBF3Ztvtsz3fH6d2_QMtve15emipkg0Q_GcOAnYRMJiNxaUg==" --local rdbms
# PASSWORD = "gAAAAABhslbL_Fm-ltNokFKpU-aAzLlLf_p2CgnQGcuxvmfVuyB0jdyDnEjTx0e234TPvp089GUGMFRLekXeOkBbesT4fLOx4Q==" --ec2-root
PASSWORD = "gAAAAABhsmFX_dMbextIwiSBgAFiLYbETzMswiYB0UrUZsGUEel0hFiTHEWqlkdnxcGkNtrqCly3c4c3qPrkrsq42uukiEqlWw=="
HOST_NAME = "localhost"
PORT_NAME = "3306"
DB_NAME = "RDMS"
TABLE_NAME = "studentDetails"

# TABLE PROPERTIES
COLOUMN_NAMES = "registrationId,rollNumber,firstName,surName,email,mobileNumber,aadhar,PAN,passport,nationality,isAadhar,isPAN,isPassport,\
isIndian,fathersName,mothersName,permanantAddress,residentialAddress,tenthCGPA,twelfthCGPA,tenthGrade,twelfthGrade,firstSemCGPA,secondSemCGPA,\
thirdSemCGPA,fourthSemCGPA,fifthSemCGPA,sixthSemCGPA,seventhSemCGPA,eightthSemGCPA,isDiploma,diplomaMarks,isBacklog,numberOfBacklogs,activeBacklog,\
PassiveBacklog,isYD,YDYears,isEducationGap,educationGapYears,isPICTStudent,currentBatch"

PII_COL_STRING = "firstname,surname,email,mobileNumber,aadhar,PAN,passport,permanantAddress,residentialAddress"
PII_COL_LIST = ['firstname','surname','email','mobileNumber','aadhar','PAN','passport','permanantAddress','residentialAddress']

MANDATORY_COL_TO_BE_SENT = ["registrationId","rollNumber","firstname","surname"]

# COMMANDS TOBE EXECUTED
# Command to get Lower Bound
GET_LOWER_BOUND_QUERY = "SELECT MAX(rollNumber) FROM {}"

# Command to Insert Dummy Data
INSERT_DATA_QUERY = "INSERT INTO {} ({}) VALUES {}"

# SELECT QUESRY
SELECT_QUERY = "SELECT {} FROM {} WHERE registrationId in ({})"

# ==============================================================
# =========== DUMMY DATA PROPERTIES ==============
# ==============================================================
NUMBER_OF_DUMMY_DATA_TOBE_INSERTED = 10
EMAIL_PREFIX_LENGTH = 9
MOBILE_LENGTH = 10
AADHAR_LENGTH = 14
PAN_LENGTH = 10
PASSPORT_LENGTH = 8
REGISTRATION_NUMBER_LENGTH = 5
ADDRESS_LENGTH = 10

# ==============================================================
# =========== ENCRYPTION AND DECRYTION PROPERTIES ==============
# ==============================================================
decreptionKey = "tN9oA_eCulJhWOF_gKEs3FdFUHzIfuj0JmDgjS-DWxo="

#================================================================
#===================Send email===================================
#================================================================
from_email='no.reply.tnpproject@gmail.com'
to_emails=['aadityab134@gmail.com','danimanas28@gmail.com','bamey2241997@gmail.com']
emailNotificationAPIKey = "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"

#================================================================
#============== FILE OPERATIONS RELATED PRPERTIES ===============
#================================================================
FILE_NAME_OF_FILE_TOBE_PARSED = "InterestedStudents.csv"
INPUT_DIR_PATH = "\\rdbms\\input\\"
INPUT_FOLDER_PATH = BASE_DIR + INPUT_DIR_PATH
INTERESTED_STUDENTS_FILE_PATH = INPUT_FOLDER_PATH + FILE_NAME_OF_FILE_TOBE_PARSED

PROJECT_PATH_FOR_CSV_FILE = "\\backEnd\\outputs\\"
OUTPUT_CSV_FILE_NAME="StudentDetails.csv"
PATH_TO_CSV_FILE = BASE_DIR + PROJECT_PATH_FOR_CSV_FILE + OUTPUT_CSV_FILE_NAME
