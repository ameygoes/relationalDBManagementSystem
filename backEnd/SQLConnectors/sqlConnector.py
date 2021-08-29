# Import Builtin Packges
import sys
import mysql.connector

# Add path to Functions
sys.path.append("../propertyFiles")

# Import Userdefined Functions
from EnvironmentVariables import *

# EXECUTE COMMAND TO INSERT VALUES
def executeInsertCommand(command):
    # Open SQL Connection
    sqlConnector = mysql.connector.connect(host=hostName, user=dbUserName, passwd=password, database=dbName, port=portName)
    mycursor = sqlConnector.cursor()

    # Execute Command
    mycursor.execute(command)

    # Insert into DB
    sqlConnector.commit()

    # Fetch from Table and return one Row
    returnOneRow = mycursor.fetchone()

    # Close the Connection
    mycursor.close

    # Return one Row
    return returnOneRow


# EXECUTE COMMAND TO GET VALUES
def executeGetCommand(command):
    # Open SQL Connection
    sqlConnector = mysql.connector.connect(host=hostName, user=dbUserName, passwd=password, database=dbName, port=portName)
    mycursor = sqlConnector.cursor()

    # Execute Command
    mycursor.execute(command)

    # Fetch from Table and return one Row
    returnOneRow = mycursor.fetchone()

    # Close the Connection
    mycursor.close

    # Return one Row
    return returnOneRow
