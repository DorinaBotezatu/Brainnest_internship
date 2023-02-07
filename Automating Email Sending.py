''' You work at a company that sends daily reports to clients via email. The goal of this project is to automate the process of sending these reports via email.

Here are the steps you can take to automate this process:

    Use the smtplib library to connect to the email server and send the emails.

    Use the email library to compose the email, including the recipient's email address, the subject, and the body of the email.

    Use the os library to access the report files that need to be sent.

    Use a for loop to iterate through the list of recipients and send the email and attachment.

    Use the schedule library to schedule the script to run daily at a specific time.

    You can also set up a log file to keep track of the emails that have been sent and any errors that may have occurred during the email sending process. '''

import smtplib, ssl
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import schedule
import time
import logging

logging.basicConfig(filename="log.txt", level=logging.DEBUG,
                    format="%(asctime)s %(message)s")


def attach_file_to_email(msg, filename):
    # Open the attachment file for reading in binary mode, and make it a MIMEApplication class
    with open(filename, "rb") as f:
        file_attachment = MIMEApplication(f.read())
    # Add header/name to the attachments
    file_attachment.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    msg.attach(file_attachment)


def send_message():
    recipients = ["valeriu.sinelnicov@gmail.com"]
    port = 587
    smtp_server = "smtp.gmail.com"
    sender_email = "botezatudorinaa@gmail.com"
    password = "" \
               "********"

    try:
        for recipient in recipients:
            msg = MIMEMultipart()
            msg['Subject'] = 'This is my Automating File Transfer project'
            msg['From'] = sender_email
            msg["To"] = recipient
            body = "Hello\
         \nThis is an automated message from Python!!!\
                   \nThank you!"
            msg.attach(MIMEText(body, 'plain'))
            attach_file_to_email(msg, "body_message.text")

            with smtplib.SMTP(smtp_server, port) as server:
                server.starttls()
                server.login(sender_email, password)
                server.send_message(msg)
                logging.info(f"Email successfully sent to {recipient}!")
    except Exception as error:
        logging.error(f"The program encountered an error: {error}")


if __name__ == '__main__':
    schedule.every().day.at("00:33").do(send_message)

    while True:
        schedule.run_pending()
        time.sleep(1)
