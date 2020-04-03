
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl

def Create_message(name, address):
    msg = MIMEMultipart("alternative")
    link = "<a href='https://www.google.com/'>here</a>"
    raw_link = 'here: https://www.google.com/'
    message = "Hello, dear %s! Thank you for your subscription. You can see your QR-code below.<br>To unsubscribe, click %s" % (name, link)
    raw = "Hello, dear %s! Thank you for your subscription. You can see your QR-code below.\nTo unsubscribe, click %s" % (name, link)
    # setup the parameters of the message
    password = "StrCpPy24rh^"
    msg['From'] = "pshtest@mail.ru"
    msg['To'] = address
    msg['Subject'] = "Your discount code"
 
    # add in the message body
    msg.attach(MIMEText(raw, 'plain'))
    msg.attach(MIMEText(message, 'html'))
    
 
    #create server
    Context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.mail.ru', 465, context = Context) as server: #587 порт - защищенный TLS 465
 
    #server.starttls() #для gmail
    
        # Login Credentials for sending the mail
        server.login(msg['From'], password)
 
 
        # send the message via the server.
        server.sendmail(msg['From'], msg['To'], msg.as_string())
 
        server.quit()
 
        print("successfully sent email to %s:" % (msg['To']))

Create_message("Pasha", "emshanov9@gmail.com")
