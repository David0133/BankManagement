import random


# Features class for some variable declaration and functions
class Features:
    account_detail = []

    def append(self, item):
        self.account_detail.append(item)

    def delete(self, num):
        for i, o in enumerate(self.account_detail):
            if o.num == num:
                del self.account_detail[i]
                print("Account deleted successfully")
                break
            else:
                print("No account found please check your account number")


# making class object
feature = Features()


# Account class for account detail initialization
class Account:
    def __init__(self, account_num, name, mobile, pan, email):
        self.num = account_num
        self.name = name
        self.mobile = mobile
        self.pan = pan
        self.email = email


"""
Function for account opening process
"""


def account_opening():
    while True:
        account_holder_name = str(input("Enter Your good name\n"))
        mobile_number = int(input("Enter your mobile number\n"))
        pan_card = int(input("Enter Pan card Number\n"))
        email_id = list(input("Your email id\n"))

        print(f"Check the details to confirm \n"
              f"Name : {account_holder_name}\n"
              f"Mobile : {mobile_number}\n"
              f"Pan card : {pan_card}\n"
              f"Email id : {email_id}\n")
        confirm = input("Enter your response Y for yes N for No - ")
        rs = confirm.lower()
        if rs == "y":
            account_number = random.randint(0, 100000000000) * 10
            feature.account_detail.append(
                Account(account_number, account_holder_name, mobile_number, pan_card, email_id))
            print(f"Note your account number - {account_number}")
            break
        else:
            print("Re-enter your detail's")
            continue


# Function for account details
def account_detail(account_num):
    for i in feature.account_detail:
        if i.num == account_num:
            print(f"******** Your Account Details **********\n"
                  f"Your name - {i.name}\n    "
                  f"Your Mobile - {i.mobile}\n"
                  f"Your Pan Card - {i.pan}\n "
                  f"Your Email - {i.email}\n  ")
            return
        else:
            continue
    print(f"No such account found with the number {account_num}")
