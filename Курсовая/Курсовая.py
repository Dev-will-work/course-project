
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl
import collections
import psycopg2
from psycopg2 import sql
from psycopg2.extras import DictCursor

def Create_message(name, address):
    msg = MIMEMultipart("alternative")
    link = "<a href='https://www.google.com/'>здесь</a>"
    raw_link = 'здесь: https://www.google.com/'
    message = "Здравствуйте, %s! Благодарим вас за подписку на нашу рассылку.<br>Вы можете взять свой QR-код здесь.<br> Чтобы отписаться от рассылки нажмите %s" % (name, link)
    raw = "Здравствуйте, %s! Благодарим вас за подписку на нашу рассылку.\n Вы можете взять свой QR-код здесь.\nЧтобы отписаться от рассылки нажмите %s" % (name, link)
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
    ##    values = [
    ##        ('mom', 'mom', 'mom', '1999-01-08', 'M', 'six@nine.com', 'ololo', False, 5 )
    ##        ]
    ##    insert = sql.SQL('INSERT INTO users VALUES {}').format(sql.SQL(',').join(map(sql.Literal, values)))
    ##    cursor.execute(insert)

def Get_table(_dbname, _user, _password, _host): #То, что изначально было
    conn = psycopg2.connect(dbname=_dbname, user=_user, 
                        password=_password, host=_host)
    cursor = conn.cursor(cursor_factory = DictCursor)
    cursor.execute('SELECT * FROM public.users')
    records = cursor.fetchall()
    cursor.close()
    conn.close()
    return records

def Print_table(_dbname, _user, _password, _host):
    conn = psycopg2.connect(dbname=_dbname, user=_user, 
                        password=_password, host=_host)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM public.users')
    for row in cursor:
        print(row)
    cursor.close()
    conn.close()

def Set_mail_off(_dbname, _user, _password, _host, id):
    conn = psycopg2.connect(dbname=_dbname, user=_user, 
                        password=_password, host=_host)
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET MAILING = False WHERE "ID" = %s' % id)
    cursor.execute('SELECT * FROM public.users')
    conn.commit()
    cursor.close()
    conn.close()

def Set_mail_on(_dbname, _user, _password, _host, id):
    conn = psycopg2.connect(dbname=_dbname, user=_user, 
                        password=_password, host=_host)
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET MAILING = False WHERE "ID" = %s' % id)
    cursor.execute('SELECT * FROM public.users')
    conn.commit()
    cursor.close()
    conn.close()

def Change_db_user(_dbname, _user, _password, _host, username): #Проработало, но результат не дало, пока хз почему
    conn = psycopg2.connect(dbname=_dbname, user=_user, 
                        password=_password, host=_host)
    cursor = conn.cursor()
    cursor.execute('ALTER DATABASE %s OWNER TO %s' % (_dbname, username)) 
    conn.commit()
    cursor.close()
    conn.close()

data = Get_table('coursework', 'pasha', 'P4h0A0e0', 'eaplfm.com')
Print_table('coursework', 'pasha', 'P4h0A0e0', 'eaplfm.com')
for row in data:
    if row['mailing'] == True:
        print('mailed')
        #Create_message(row['name'], row['adress'])
        Set_mail_off('coursework', 'pasha', 'P4h0A0e0', 'eaplfm.com', row['ID'])
        Print_table('coursework', 'pasha', 'P4h0A0e0', 'eaplfm.com')

#Create_message("Pasha", "emshanov9@gmail.com")
#conn = Connect('coursework', 'pasha', 'P4h0A0e0', 'eaplfm.com')
#cur = Set_cursor()
#Change_db_user('coursework', 'pasha', 'P4h0A0e0', 'eaplfm.com', 'yarik')
#Close_connection(cursor)
