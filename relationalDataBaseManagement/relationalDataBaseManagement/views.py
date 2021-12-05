import sys
import os

sys.path.append('C:\\Users\\lenovo\\data structure in python\\BE project\\relationalDBManagementSystem')
sys.path.append('C:\\Users\\lenovo\\data structure in python\\BE project\\relationalDBManagementSystem\\relationalDataBaseManagement\\relationalDataBaseManagement')
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from backEnd.DummyDataGenerate.DummyDataGeneration import getStudentDetailsCSV
from backEnd.Processors.SendEmailNotification.sendEmail import sendMailUsingSMTP
from settings import *




def home(request):
    return(render(request, "home.html", {"text":"home"}))

def index(request):
    if request.method=="POST" and request.FILES["studentIds"]:
        inputFields = request.POST.getlist('inputFields')
        toemail = request.POST.getlist('email')
        inputeCSVFile = request.FILES["studentIds"]
        fs = FileSystemStorage(location=MEDIA_ROOT)
        filename = fs.save(inputeCSVFile.name, inputeCSVFile)
        file_url = fs.url(filename)
        # one = os.path.exists('C:/Users/lenovo/data structure in python/BE project/relationalDBManagementSystem/relationalDataBaseManagement/input')
        # print(one)
        getStudentDetailsCSV(inputFields)
        # sendMailUsingSMTP()
        return(render(request, "home.html", {"text":"Your Email was sent to: {% toemail %}"}))
    return(render(request, "index.html"))
