import account as acc, pandas as pd, os
import emailing


RECPTNS = []


def main(message = "Which account do you want to use? OLD | NEW\n"):
    action = input(message)
    if action.lower() == "old":
        get_creds()
        recptns(0)
        
    elif action.lower() == "new":
        acc.create()
    else: main('Please enter a valid selection - OLD | NEW\n')


def get_creds():
    global INFO
    if not os.path.exists('info.pickle'):
        acc.create()
    creds = acc.retrieve()
    recptns(0, creds[0]['email'], creds[1], creds[0]['host'], creds[0]['port'])


def recptns(count, *info):
    global RECPTNS
    num = int(input("Enter the number of recipients: "))
    if count < 2:
        for i in range(num):
            RECPTNS.append(input("Enter the email id of receiver {}: ".format(i+1)))
        RECPTNS = set(RECPTNS)
        emailing.init(info, RECPTNS)
        quit()

    else:
        print("ERR500: REACHED MAXIMUM ATTEMPTS LIMIT")
        quit()


if __name__ == "__main__": main()
