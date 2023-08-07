import smtplib

def send_email(sender, receiver, password, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender, password)
    message = f"Subject: {subject}\n\n{message}"
    server.sendmail(sender, receiver, message)
    print("Email sent!")
    server.quit()


sender ="SENDER_ADDRESS"
receiver = "RECEIVER_ADDRESS"
password = "APP-PASSWORD"
subject = "Hello From GFG"
message = "Message Body"