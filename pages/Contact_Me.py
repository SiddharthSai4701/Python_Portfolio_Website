import streamlit as st
from send_email import send_email
st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Enter your email ID")
    text = st.text_area("Your message")
    button = st.form_submit_button()

    message = f"""\
Subject: Python Portfolio Website has a response from {user_email}

From: {user_email}
{text}
"""
    if button:
        send_email(message)
        st.info("Email sent successfully!")