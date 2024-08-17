import smtplib, ssl
import os

def send_email(message):

    host = "smtp.gmail.com"
    port = 465

    username = "sidvsai@gmail.com"
    password = os.getenv("PYTHON_PORTFOLIO_SITE_PASSWORD")

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        # Sending the mail to myself when a user wants to contact me. Therefore from and to addresses are the same
        server.sendmail(username, username, message)