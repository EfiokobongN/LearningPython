import smtplib
from email.message import EmailMessage

sender = "from@example.com"
receiver = input('enter the receiver email address:-')
body = input('enter the message you want to send:-')

def sendMail(receiver, body):
    msg = EmailMessage()
    msg["Subject"] = "Test Mailtrap Email"
    msg["From"] = sender
    msg["To"] = receiver
    msg.set_content(body)

    try:
        with smtplib.SMTP('sandbox.smtp.mailtrap.io', 587, timeout=20) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login('name', 'password')
            server.send_message(msg)
        print("Email sent successfully. Check your Mailtrap inbox.")
    except Exception as error:
        print(f"Email sending failed: {error}")

sendMail(receiver, body)