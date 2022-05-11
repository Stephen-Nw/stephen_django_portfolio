import os
import smtplib

MY_EMAIL = os.environ.get('EMAIL')
MY_PASSWORD = os.environ.get('PASSWORD')


def send_email(name, email, subject, message):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                            msg=f"Subject: New Contact\n\nYou have a new project request:\nName - {name}\nEmail - {email}\nSubject - {subject}\nMessage - {message}")
