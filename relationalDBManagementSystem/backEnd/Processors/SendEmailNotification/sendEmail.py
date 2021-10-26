import os
import sys
import base64
from datetime import date
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, FileContent, FileName, FileType, Disposition)

sys.path.append('../../propertyFiles')
from EnvironmentVariables import *


def sendmail():
    message = Mail(
        from_email,
        to_emails,
        subject='PFA Student Details for {}'.format(date.today()),
        html_content='<strong>PFA student details</strong>'
    )

    with open('../FileParsers/DecryptedCSV.csv', 'rb') as f:
        data = f.read()
        f.close()
    encoded_file = base64.b64encode(data).decode()

    attachedFile = Attachment(
        FileContent(encoded_file),
        FileName('studentDetails.csv'),
        FileType('application/csv'),
        Disposition('attachment')
    )
    message.attachment = attachedFile

    sg = SendGridAPIClient(emailNotificationAPIKey)
    response = sg.send(message)
    print(response.status_code, response.body, response.headers)


sendmail()
