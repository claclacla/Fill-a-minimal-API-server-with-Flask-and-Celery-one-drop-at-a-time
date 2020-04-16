import os

from MockSMTP import MockSMTP

from celery import Celery

app = Celery('tasks', broker='amqp://rabbitmq:5672')

@app.task
def send_signup_email(receiverEmail):
    sender = "Simone Adelchino <from@claclacla.com>"
    receiver = "<" + receiverEmail + ">"

    message = f"""\
Subject: Hi {receiverEmail}
To: {receiver}
From: {sender}

Registration Successful!"""

    try:
        mockSMTP = MockSMTP(os.environ["SMTP_ADDRESS"], os.environ["SMTP_PORT"])
        mockSMTP.login(os.environ["SMTP_USERNAME"], os.environ["SMTP_PASSWORD"])
        mockSMTP.sendmail(sender, receiver, message)
        mockSMTP.close()  

        print("Successfully sent email")
    except smtplib.SMTPException:
        print("Error: unable to send email")