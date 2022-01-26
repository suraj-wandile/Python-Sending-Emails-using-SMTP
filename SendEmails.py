import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#(https://www.courier.com/blog/three-ways-to-send-emails-using-python-with-code-tutorials/)
#1. Set up a Gmail account for sending your emails. Since you’ll be feeding a plaintext password to the program, Google considers the SMTP connection less secure. 
#2. Go to the account settings and allow less secure apps to access the account. As an aside, Gmail doesn't necessarily use SMTP on their internal mail servers; however, Gmail SMTP is an interface enabled by Google's smtp.gmail.com server.

SenderAddress = "example@gmail.com" #Your Email Address
password = "Your_Password" #Your Password
df = pd.read_csv('email_ids.csv')
emails = df['email_addr'].values
for email in emails:
    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = SenderAddress
    message['To'] = email
    message['Subject'] = "Your Subject" # The subject line
    mail_content = "Body Content" # The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    text = message.as_string()
    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) # use gmail with port
    session.starttls()  # enable security
    session.login(SenderAddress, password) # login with mail_id and password
    session.sendmail(SenderAddress, email, text)
    print(email) #email-id just sent
    session.quit()