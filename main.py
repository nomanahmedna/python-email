#python email sending 

import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart



def email_sender(to):
    server = smtplib.SMTP('smtp.titan.email',587) #configure your email ID with YOUR SMTP Contact Your WebMaster

    server.ehlo

    server.login('youremail@emaildomain.com','enteryourpassword') #Sender_email_id, #password

    msg = MIMEMultipart()

    msg['from'] = 'no-reply' #FROM_Name_TO_Appear_inBOX
    msg['to'] = to
    msg['subject'] = 'ENTER YOUR EMAIL Subject HERE'

    with open('msg.txt',"r") as f:
        message = f.read()

    msg.attach(MIMEText(message,'plain'))

    filename = 'YOUR-EMAIL-Attachment-IMAGE.png'
    attachment = open(filename,'rb')

    p = MIMEBase('application','octet-stream')
    p.set_payload(attachment.read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition',f'attachment; filename={filename}')
    msg.attach(p)
    text = msg.as_string()
    server.sendmail('YOUR_SENDER_EMAIL_ID',to,text)

email_sender('YOUR_SENDER_EMAIL_ID')
