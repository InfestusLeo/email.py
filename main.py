import smtplib as s
import account as a
import os
import datetime as d
#from queue import Queue as q

HOST = ''
SENDER_EMAIL = ''
SENDER_PASSWORD = ''
PORT = ''
RECEPIENT = ''
MESSAGE = ''


def initialize():
    if os.path.isfile("sender_credentials.txt"):
        a.boot()
    else:
        a.setup_account()


def extract_info():
    global HOST, SENDER_EMAIL, SENDER_PASSWORD, PORT
    HOST = a.parse_info('HOST')
    SENDER_EMAIL = a.parse_info('SENDER_EMAIL')
    SENDER_PASSWORD = a.parse_info('SENDER_PASSWORD')
    PORT = a.parse_info('PORT')
    print("Will be sending the mail from {} account".format(SENDER_EMAIL))
    send_email()


#def extract_recepients():
    #pass


def send_email():
    global RECEPIENT,MESSAGE
    RECEPIENT = input("Enter the email address of the recipient: ")
    MESSAGE = input("Enter your message: ")
    soc = s.SMTP(HOST,PORT)
    print(soc.ehlo())
    print(soc.starttls())
    print(soc.login(SENDER_EMAIL,SENDER_PASSWORD))
    soc.sendmail(SENDER_EMAIL,RECEPIENT,MESSAGE)
    print("Your message has been sent to {}".format(RECEPIENT))
    print(soc.quit())
    write_log(RECEPIENT,MESSAGE)

def write_log(*args):
    f = open("log.txt","a")
    f.write(str(d.datetime.now())+"\n")
    f.write("RECIPIENT: {}\nMESSAGE: {}\n\n".format(RECEPIENT,MESSAGE))


if __name__ == "__main__": initialize()