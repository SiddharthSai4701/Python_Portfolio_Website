import streamlit as st
# from send_email import send_email
from email.mime.text import MIMEText

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
        
st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Enter your email ID")
    body = st.text_area("Your message")
    text = MIMEText(body)
    button = st.form_submit_button()

    message = f"""\
Subject: Python Portfolio Website has a response from {user_email}

From: {user_email}
{text}
"""
    if button:
        send_email(message)
        st.info("Email sent successfully!")