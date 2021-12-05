import random
import string
import pandas as pd
import sys
from Names import *


def getFirstname():
    MaleFirstName = random.choice(MaleName)
    FemaleFirstName = random.choice(FemaleName)
    ChoiceOfName = [MaleFirstName,FemaleFirstName]
    FinalFirstNameChoice = random.choice(ChoiceOfName)
    return FinalFirstNameChoice

def getFatherName():
    FatherName = random.choice(MaleName)
    return FatherName

def getMotherName():
    MotherNameSelection = random.choice(FemaleName)
    return MotherNameSelection

def getSurname():
    SurName = random.choice(lastName)
    return SurName
#========================== MARKS =============================
def getCgpa():
    firstCGPA = round(random.uniform(6.0, 10.0),1)
    return firstCGPA

def getMarks():
    RandomGrade = round(random.uniform(55.0, 99.9),1)
    return RandomGrade

def getRegistrationId():
    regisId = random.randint(0,2)
    return regisId

def getRandomAlphaNum(len):
    return ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k = len))

def getRandomNum(len):
    return ''.join(random.choices(string.digits, k = len))

def getAddress(len):
    return ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = len))

def getRollno():
    return random.randint(40000,49999)

def readInputCSV():
    list = []
    toConvertToString="'{}'"
    dg = pd.read_csv("C:/Users/lenovo/data structure in python/BE project/relationalDBManagementSystem/relationalDataBaseManagement/input/regisN.csv")
    for index, row in dg.iterrows():
        list.append(toConvertToString.format(row[0]))
    return','.join(list)
