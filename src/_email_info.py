import smtplib
import email,ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import os
import dotenv
dotenv.load_dotenv()

#def send_email(text,text1):
subject="Test email"
body = """\
    This is a test email
    """
text = 'Holita'
sender_email = 'sensoatest@gmail.com'
receiver_email = 'anasenso@gmail.com'
password = os.getenv("EMPASS")

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
   
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, body)
