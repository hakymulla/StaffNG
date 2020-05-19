import sys
import os
import random

class Color:
    LOGIN = '\33[34m'
    CREATE = '\033[33m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'


class Welcome:

    def __init__(self):

        print(Color.LOGIN + ''' 
        Welcome
        {1}---Staff Login
        {2}---Close App  
        ''' + Color.END)

        staff_input = input('Enter Here: ')
        if staff_input == str(1):
            StaffLogin()
            # print('1 selected')
        elif staff_input == str(2):
            sys.exit()
        else:
            self.__init__()


class StaffLogin:

    def __init__(self):
        self.username = input('Username: ')
        self.password = input('Password: ')
        self.validate()

    def validate(self):
        with open('staff.txt', 'r') as file:
            for line in file:
                username, password, _, _ = line.split(', ')
                if self.username == username and self.password == password:
                    print('Login Successful')
                    Staff(self.username)
                    break
            else:
                print('Wrong Username or Password, Try Again!!! ')
                self.__init__()


class Staff:

    def __init__(self, username):
        self.username = username
        self.usersession()
        print( Color.CREATE + """  
            {1}---Create New Bank Account
            {2}---Check Account Details
            {3}---Logout
            """ + Color.END)

        staff_select = input('Enter Here: ')
        if staff_select == str(1):
            self.createnewbankaccount()
        elif staff_select == str(2):
            self.checkaccountdetails()
        elif staff_select == str(3):
            self.logout()
        else:
            self.__init__(self.username)

    def usersession(self):
        with open(f'user_session_{self.username}', 'w') as f:
            f.write('User Session Started: ')

    def createnewbankaccount(self):

        account_name = input('Account Name: ')
        opening_balance = input('Opening Balance: ')
        account_type = input('Account Type: ')
        account_email = input('Account Email: ')
        account_number_list = [random.randint(0, 9) for _ in range(10)]
        account_number = ''.join(map(str, account_number_list))
        print(f'The Customer {account_name} has the Account Number {account_number}')

        with open(f'customer.txt', 'a+') as f:
            for detail in [account_name, opening_balance, account_type, account_email, account_number]:
                f.write(f'{detail}, ')
            f.write('\n')
        self.__init__(self.username)

    def checkaccountdetails(self):
        account_num = input('Enter Account Number: ')
        with open('customer.txt') as file:
            for line in file:
                account_name, opening_balance, account_type, account_email, account_number = line[:-3].split(',')
                if account_num == account_number.strip(' '):
                    print(f'Account Name : {account_name} \nOpening Balance : {opening_balance} \nAccount Type : {account_type} \nAccount Email : {account_email} \nAccount Number : {account_number}')
        self.__init__(self.username)

    def logout(self):
        os.remove(f'user_session_{self.username}')
        Welcome()


if __name__ == '__main__':
    Welcome()
