import smtplib as core


def init(*info):
    mod = core.SMTP(info[0][2],info[0][3])
    mod.ehlo()
    mod.starttls()
    print(mod.login(info[0][0],info[0][1]))
    msg = input("Enter your message:\n")
    for i in info[1]:
        mod.sendmail(info[0][0], i, msg)
        print("SENT!")

