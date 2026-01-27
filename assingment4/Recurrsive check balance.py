# program for mixx by Yas
print('Enter SSID code')
code = input('SSID code: ')
if code=='*150*01#':
    print('1.Send Money \n2.Buy Airtime \n3.Pay bills \n4.Check balance \n5.Exit ')
def send_money():
    user = input('Enter recipient number: ')
    if len(user)==10:
        user_1 = input('Enter amount: ')
        password=input('Enter password: ')
        if password=='0000':
            print(f'successfully sent {user_1}Tsh to {user}')
        else:
            print('wrong password try again')
    else:
        print('Invalid number')
    return
def buy_airtime():
    user_1 = input('Enter amount: ')
    password = input('Enter password: ')
    if password == '0000':
        print(f'successfully bought airtime of {user_1}Tsh')
    else:
        print('wrong password try again')
    return
def pay_bills():
    user_1 = input('Enter bill payment number: ')
    if len(user_1)==12:
        user_2 = input('Enter amount: ')
        password=input('Enter password: ')
        if password=='0000':
            print(f'successfully paid {user_2}Tsh to the {user_1} control number')
    else:
        print('Invalid number')
    return
def check_balance():
    while True:
        user_1 = input('Enter password: ')
        if user_1=='0000':
            print('your amount \n50000Tsh')
        else:
            print('wrong password try again')
        print('Do you want to continue? enter y for yes or n for no')
        user_2 = input('Enter y/n :')
        if user_2=='n':
            break

    return
def Exit():
    return
choice = input('enter your option:')
if choice=='1':
    send_money()
elif choice=='2':
    buy_airtime()
elif choice=='3':
    pay_bills()
elif choice=='4':
    check_balance()
elif choice=='5':
    Exit()
else:
    print('Invalid option')