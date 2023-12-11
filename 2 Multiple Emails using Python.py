import smtplib as s

ob = s.SMTP('smtp.gmail.com', 587)
ob.ehlo()
ob.starttls()
ob.login('native.ganesh@gmail.com', 'Gmail@3539')

subject = "Test for Multiple emails"
body = "Hello World - Native Builders"
message = "Subject: {}\n\n{}".format(subject, body)

listadd = ['nativeconsult.build1@gmail.com',
           'rehankc2052@gmail.com', 'ganeshkc2052@gmail.com']

for recipient in listadd:
    ob.sendmail('native.ganesh@gmail.com', recipient, message)
    print(f"Email sent to {recipient}")

print("Send mail to all recipients")
ob.quit()
