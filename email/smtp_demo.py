# What is SMTP?
# ------------------
# SMTP (Simple Mail Transfer Protocol) is a TCP/IP protocol used in sending
# and receiving e-mail.
# more details : https://www.youtube.com/watch?v=PJo5yOtu7o8
#
#
# I have used two built-in modules in this example : smtplib and email
#
# Module : smtplib :
# --------------------
# The smtplib is a Python library for sending emails using the Simple Mail
# Transfer Protocol (SMTP).
# link : https://docs.python.org/3/library/email.html#module-email
#
# Module : email :
# -----------------
# The email package is a library for managing email messages.
# link : https://docs.python.org/3/library/email.html#module-email
# example : https://docs.python.org/3/library/email.examples.html
#
#
# Mail server :
# ---------------
# To actually send an email, we need to have access to a mail server.
# Python comes with a simple development mail server. We can start the
# built-in mail server on port 1025 using this simple command :
# $ python -m smtpd -c DebuggingServer -n localhost:1025


import smtplib
from email.message import EmailMessage

# In our apps, we will get the values from environment variables
EMAIL_SERVER = 'localhost'  # for gmail, use smtp.gmail.com
EMAIL_SERVER_PORT = 1025  # for gmail, use 587
EMAIL_ADDRESS = 'hellogeekworld@gmail.com'
EMAIL_PASSWORD = None  # for gmail, use the mail password

msg = EmailMessage()
msg['Subject'] = 'Sending Emails With Python is Fun!'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'hellogeekworld@gmail.com'
msg.set_content('This is a simple mail by talha.')

with smtplib.SMTP(EMAIL_SERVER, EMAIL_SERVER_PORT) as smtp:
    if EMAIL_PASSWORD is not None:
        # we do not need to login to the debugging server
        # running at localhost
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)
    print("Message Sent!")
