import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json

config = json.loads(open("src/config.json").read())
config = config["email_config"]
fromaddr = config["email"]
password = config["password"]
mailing_list = config["mailing_list"]
recipients = mailing_list

def send(Subject, Message):
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = ", ".join(mailing_list)
    msg['Subject'] = Subject

    body = Message
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, password)
    text = msg.as_string()
    server.sendmail(fromaddr, recipients, text)
    server.quit()