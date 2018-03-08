import os
import sys
import smtplib
import getpass
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import datetime

COMMASPACE = ', '


def formatted_date():
    today = datetime.date.today()
    date_split = str(today).split('-')
    date_split.reverse()
    date_format = '-'.join(date_split)
    return date_format


def email_report(file_name):
    # Create the enclosing (outer) message
    sender = 'nikhilendra.g@gmail.com'
    gmail_password = getpass.getpass(prompt='Enter gmail password : ')
    recipients = ['nikhilendra.g@gmail.com']
    outer = MIMEMultipart()
    outer['Subject'] = 'Holding statement for ' + formatted_date()
    outer['To'] = COMMASPACE.join(recipients)
    outer['From'] = sender

    # List of attachments
    attachments = list()
    attachments.append(file_name)

    # Add the attachments to the message
    for file in attachments:
        try:
            with open(file, 'rb') as fp:
                msg = MIMEBase('application', "octet-stream")
                msg.set_payload(fp.read())
            encoders.encode_base64(msg)
            msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
            outer.attach(msg)
        except FileNotFoundError:
            print("Unable to open one of the attachments. Error: ", sys.exc_info()[0])
            raise

    composed = outer.as_string()

    # Send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as s:
            s.ehlo()
            s.starttls()
            s.ehlo()
            s.login(sender, gmail_password)
            s.sendmail(sender, recipients, composed)
            s.close()
        print("Email sent!")
    except:
        print("Unable to send the email. Error: ", sys.exc_info()[0])
        raise


if __name__ == '__main__':
    email_report('holdings_statement.txt')
