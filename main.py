import smtplib
import os
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
load_dotenv()
# print(os.getenv('password'))

server = smtplib.SMTP('smtp.gmail.com',587)

server.ehlo()
server.starttls()
server.ehlo()
password = os.getenv('password')
email = os.getenv('email')
target = os.getenv('receiver')
server.login(email,password)


sms = MIMEMultipart()

sms['From'] = 'DSG'
sms['To'] = 'itsdarsan09@gmail.com'
sms['Subject'] = 'Just a test '

with open('message.txt','r') as f:
    message = f.read()

sms.attach(MIMEText(message,'plain'))

text = sms.as_string()

server.sendmail(email,target, text)