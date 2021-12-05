import os
import sys
import base64
from datetime import date

# Sendgrid Dependencies
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)

# SMTP Dependencies
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import smtplib

sys.path.append('C:\\Users\\lenovo\\data structure in python\\BE project\\relationalDBManagementSystem\\backEnd\\SendEmailNotification')
from emailProperties import *

# def sendmail(path):
#     print(to_emails)
#     message = Mail(
#         from_email,
#         to_emails,
#         subject='PFA Student Details for {}'.format(date.today()),
#         html_content='<strong>PFA student details</strong>'
#     )
#
#     with open(path, 'rb') as f:
#         data = f.read()
#         f.close()
#     encoded_file = base64.b64encode(data).decode()
#
#     attachedFile = Attachment(
#         FileContent(encoded_file),
#         FileName('studentDetails.csv'),
#         FileType('application/csv'),
#         Disposition('attachment')
#     )
#     message.attachment = attachedFile
#
#     sg = SendGridAPIClient(emailNotificationAPIKey)
#     response = sg.send(message)
#     print(response.status_code, response.body, response.headers)

def sendMailUsingSMTP():
    # Create a multipart message
    msg = MIMEMultipart()
    body_part = MIMEText(MESSAGE_BODY, 'plain')
    msg['Subject'] = EMAIL_SUBJECT.format(date.today())
    msg['From'] = EMAIL_FROM
    msg['To'] = ", ".join(EMAIL_TO)
    # Add body to email
    msg.attach(body_part)
    # open and read the CSV file in binary
    with open(PATH_TO_CSV_FILE,'rb') as file:
    # Attach the file with filename to the email
        msg.attach(MIMEApplication(file.read(), Name=FILE_NAME.format(date.today())))

    # Create SMTP object
    smtp_obj = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtp_obj.connect(SMTP_SERVER,SMTP_PORT)
    smtp_obj.ehlo()
    smtp_obj.starttls()
    smtp_obj.ehlo()
    # Login to the server
    smtp_obj.login(SMTP_USERNAME, SMTP_PASSWORD)

    # Convert the message to a string and send it
    smtp_obj.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    smtp_obj.quit()
