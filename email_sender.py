import smtplib
from email.message import EmailMessage
email=EmailMessage()
email['from']='Siddhi Parte'
email['to']='siddhiparte2409@gmail.com'
email['subject']='You won 1,000,000 dollars!'

email.set_content('Have a good day')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('siddhiparte24@gmail.com',#'enter your password')
    smtp.send_message(email)
    print('all good!')
