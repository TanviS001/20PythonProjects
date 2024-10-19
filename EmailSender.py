from email.message import EmailMessage
import smtplib
import ssl

email_sender = "tanvi@gmail.com"
email_password = "nolbnwznlhbjzgdt"

email_receiver = "tan@gmail.com"

subject = "Great thing!"
body = """
Hey there, 
    Just created an EmailSender with Python.
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
  
