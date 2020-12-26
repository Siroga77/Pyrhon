import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddr = "email"
mypass = "pass"
toaddr = "email"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr

a = input("Subject: ")
msg['Subject'] = a
b = input("Message: ")
body = b

msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, mypass)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
