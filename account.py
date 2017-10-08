import hashlib as h, pandas as pd, os


EMAIL, PASS, H_PASS, SHost, PORT = '', '', '', '', ''


def log_in(info,choice,attempts):
    global PASS, H_PASS, SHost, PORT
    TEMP_PASS = input('Enter your password: ')
    H_PASS = h.sha256(TEMP_PASS.encode('utf-8')).hexdigest()
    if H_PASS == info.loc[choice].passwd:
        PASS = TEMP_PASS
        SHost = info.loc[choice].host
        PORT = info.loc[choice].port
        return True
    else:
        print("ERR404: PASSWORD MISMATCH")
        if(attempts < 3):
            log_in(info,choice,attempts+1)
        else:
            print("ERR500: REACHED MAXIMUM ATTEMPTS LIMIT")
            quit()


def retrieve():
    global EMAIL
    if os.path.exists('info.pickle'):
        info = pd.read_pickle('info.pickle')
        kw = list(info['email'].index)
        for i in kw: print(i, end="\t\t")
        choice = input('\nWhich account do you want to use (Specify the tag)?\n')
        EMAIL = info.loc[choice].email
        print("You will be using {}".format(EMAIL))
        status = log_in(info,choice,1)
        if status:
            return(info.loc[choice].to_dict(), PASS)
            
    else:
        print('ERR102: No Accounts have been set up yet. Please set up an account.')
        create()


def store():
    old_info = pd.DataFrame()
    tag = input('Enter the tag, to store the data with: ')
    data = {
        'email': EMAIL,
        'passwd': H_PASS,
        'host': SHost,
        'port': PORT
        }
    frame = pd.DataFrame(data, index = [str(tag)])
    if os.path.exists('info.pickle'):
        old_info = pd.read_pickle('info.pickle')
    summed = pd.concat([old_info,frame])
    summed.to_pickle('info.pickle')


def create():
    global EMAIL, PASS, H_PASS, SHost, PORT
    EMAIL = input("Enter your email: ")
    PASS = input("Enter your password: ")
    TEST_PASS = input("Confirm your password: ")

    if PASS == TEST_PASS:
        SHost = input("Enter your SMTP Host: ")
        PORT = input("Enter the port: ")
        H_PASS = h.sha256(PASS.encode('utf-8')).hexdigest()
        store()
        
    else:
        print("ERR101: PASSWORD MISMATCH.")
        quit()


#create()
#retrieve()
