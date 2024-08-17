# dakq zxsq izsv mkyl
import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "sidvsai@gmail.com"
password = "dakq zxsq izsv mkyl"

receiver = "siddharthvsai@gmail.com"

context = ssl.create_default_context()

message = """\
Subject: Test Email
Hi!
How are you?
Bye!
"""
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)