import smtplib
import email,ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from analysis import *
from barcharts import *
from analysis2 import *


def send_email(text,text1):
    subject="Test email"
    body = """\
    This is a test email
    """
    sender_email = 'sensoatest@gmail.com'
    receiver_email = 'anasenso@gmail.com'
    password = os.getenv("EMPASS")

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    # message.attach(MIMEText(body, "plain"))
    # filename = "Top 10 players.png"
    # with open(filename, "rb") as attachment:
    #     part = MIMEBase("application", "octet-stream")
    #    part.set_payload(attachment.read())
    # encoders.encode_base64(part)
    # part.add_header(
    #     "Content-Disposition",
    #     f"attachment; filename= {filename}",
    # )
    # message.attach(part)
    text = message.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
