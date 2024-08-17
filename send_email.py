import smtplib, ssl


def send_email(receiver, message):

    host = "smtp.gmail.com"
    port = 465



    # receiver = receiverID

    context = ssl.create_default_context()

    mail_message = """\
    Subject: Portfolio site has a response
""" + message + '\n' + receiver
    # message = """\
    # Subject: Test Email
    # Hi!
    # How are you?
    # Bye!
    # """
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        # Sending the mail to myself when a user wants to contact me
        server.sendmail(username, username, mail_message)