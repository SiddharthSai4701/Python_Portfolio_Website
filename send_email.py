import smtplib, ssl
import os
from dotenv import load_dotenv

def send_email(message):

    load_dotenv()

    host = "smtp.gmail.com"
    port = 465

    username = "sidvsai@gmail.com"
    password = os.getenv("PASSWORD")

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        # Sending the mail to myself when a user wants to contact me. Therefore from and to addresses are the same
        server.sendmail(username, username, message)