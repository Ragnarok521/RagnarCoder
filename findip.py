
try:

    import time
    import os
    import socket as s

    Password = '521'

    os.system('clear')

    P=input('Password >>> : ')

    time.sleep(1.50)
    os.system('clear')
    print('wait ...')
    time.sleep(2)
    os.system('clear')
    if P==Password:
        print('Login')
        time.sleep(2)
        os.system('clear')
        host = input('Enter Web Name >>> :  ')

        time.sleep(2)
        os.system('clear')
        print('wait ...')
        time.sleep(2)
        os.system('clear')

        print((f'\033[1;94mip = {s.gethostbyname(host)}'))

    else:
        print('Failed')

except:
    print('Error')