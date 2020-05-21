import smtplib
from email.message import EmailMessage
import email,ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import os
import dotenv
from email.utils import formatdate
dotenv.load_dotenv()

sender_email = 'sensoatest@gmail.com'
receiver_email = 'anasenso@gmail.com'
password = os.getenv("EMPASS")

#body = 

def dim_email(text):
    msg = MIMEMultipart()
    msg["Subject"] = f'Factor Analysis: Dimension deep-dive'
    msg["Date"] = formatdate(localtime=True)
    msg.attach(MIMEText(f'Hello,\n\nHere you have the item Factor Analysis:\n\n\n{text}'))
    
    #Send mail 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()

def it_email(text):
    msg = MIMEMultipart()
    msg["Subject"] = f'Factor Analysis: Item deep-dive'
    msg["Date"] = formatdate(localtime=True)
    msg.attach(MIMEText(f'Hello,\n\nHere you have the item Factor Analysis\n\n\n\n{text}'))
    
    
    #Send mail 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()


