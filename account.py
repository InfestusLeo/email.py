import main as m


def setup_account():
    m.SENDER_EMAIL = input("Enter your email address: ")
    m.SENDER_PASSWORD = input("Enter your password: ")
    m.HOST = input("Enter your SMTP server host name: ")
    m.PORT = input("Enter the port number: ")
    f = open("sender_credentials.txt", "w")
    f.write("#Sender's email\nSENDER_EMAIL={}\n\n".format(m.SENDER_EMAIL))
    f.write("#Sender's password\nSENDER_PASSWORD={}\n\n".format(m.SENDER_PASSWORD))
    f.write("#Sender's host\nHOST={}\n\n".format(m.HOST))
    f.write("#Sender's port\nPORT={}\n\n".format(m.PORT))
    f.close()
    m.send_email()


def parse_info(query):
    with open("sender_credentials.txt","rt") as r:
        for line in r.readlines():
            if query in line:
                result = line.split("=")
                return result[-1].strip().replace("\n","")


def boot():
    choice = input("Do you want to use a new account or use an already saved one? OLD | NEW\n")
    if choice.lower() == "new":
        setup_account()
    elif choice.lower() == "old":
        m.extract_info()
    else:
        print("Please enter a valid selection.")
        boot()