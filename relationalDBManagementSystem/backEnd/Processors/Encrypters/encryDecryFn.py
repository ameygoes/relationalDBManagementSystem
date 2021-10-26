import sys
import pandas as pd
import string

sys.path.append("../../propertyFiles")
sys.path.append("../../SQLConnectors")
sys.path.append("../../DummyDataGenerate")

from Encryption import *
from dummyDataPayload import *


# reqCols = [firstname,surname,email,mobileNumber,
# actualReqCols = [rollNumber,registrationId]
piiColumns = [firstname,surname,email,aadhar,PAN,passport,mobileNumber,permanantAddress,residentialAddress]


def fillEnctryptedValues(alphaNumericEmail,dynamicNumber):

    encrypted = []

    # GO THOUGH LOOP OF COLOUMNS AND ENCRYPT VALUES
    for colName in piiColumns:
        # CHECK IF COLOUMN IS EMAIL VARIABLE IF IT IS REPLACE IT WITH ALPHANUMERCAL EMAIL
        if(colName == email):
            Colvalue = colName.format(alphaNumericEmail)
        # IF COLOUMN IS NOT EMAIL REPLACE IT WITH DYNAMICNUMBER
        else:
            Colvalue = colName.format(dynamicNumber)

        # GET ENCRYPTED VALUE OF COLOUMN FROM PIIDATA
        encryptedValue = wrapperEncryptFunction(Colvalue)

        # APPEND IT TO ENCRYPTED ARRAY
        encrypted.append(encryptedValue)
    return encrypted
