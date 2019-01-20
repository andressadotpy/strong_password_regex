import pdb
import re

pdb.set_trace()

def strong_password_regex(pword):
    strong_password  = re.compile(r'''((?=.*[A-Z])
    (?=.*[0-9))
    (?=.*[a-z])
    )''', re.VERBOSE)
    mo = strong_password.search(pword)
    if (mo == None):
        return False
    else:
        print('Great!')
        return True


password = input('Please, type password: ')
if (len(password) >= 8):
    num = strong_password_regex(password)
    if (num == False):
        print('Weak password.')
        print(num)
    elif (num == True):
        print('Good password. Access granted')
else:
    print('Password must have 8 or more characters.')


