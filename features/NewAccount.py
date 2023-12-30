import datetime
from datetime import datetime
import random
from pytz import timezone
from turtle import clear

import exception.fileException
import os
import time, sys

# Global variable
date =  datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')

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

    def __init__(self, account_num, name, mobile, pan, email, balance):
        self.num = account_num
        self.name = name
        self.mobile = mobile
        self.pan = pan
        self.email = email
        self.balance = balance


"""
Function for account opening process
"""


def account_opening():
    while True:
        account_holder_name = ""
        mobile_number = 0
        pan_card = 0
        email_id = ""
        balance = 0.0
        conv = ""
        size = 0

        try:
            while True:
                try:
                    try:
                        account_holder_name = input("Enter Your good name\n")

                        if account_holder_name == "":
                            raise exception.fileException.EmptyString("Blank input is not allowed")
                        elif account_holder_name.isdigit():
                            raise exception.fileException.NumNotAllow("Name does not contains Numbers")
                        else:
                            break
                    except exception.fileException.EmptyString as empty:
                        print(empty)

                except Exception:
                    print("Not valid")
                except exception.fileException.EmptyString as empty:
                    print(empty)

            while True:
                try:
                    try:
                        mobile_number = int(input("Enter your mobile number\n"))
                        conv = str(mobile_number)
                        d = len(conv)
                    except ValueError:
                        print("Enter a valid mobile number")
                        continue
                    if d != 10:
                        raise exception.fileException.NotValidMob("The mobile number is of 10 Digits\n")
                    else:
                        break
                except exception.fileException.NotValidMob as c:
                    print(c)

            while True:
                try:
                    try:
                        pan_card = int(input("Enter Pan card Number\n"))
                        conv = str(pan_card)
                        size = len(conv)
                    except ValueError:
                        print("Alphabets are not allowed")
                        continue
                    if size != 10:
                        # print("Pan Card should be of 10 digit's and does not contains Alphabets")
                        raise exception.fileException.WrongInput("Pan card should be of 10 Digit long")
                    else:
                        break

                except exception.fileException.WrongInput as a:
                    print(a)

            while True:
                email_id = str(input("Your email id\n"))
                try:
                    if email_id == "":
                        raise exception.fileException.EmptyString("Enter a valid email-id")
                    else:
                        break
                except exception.fileException.EmptyString as e:
                    print(e)
                    continue

            while True:
                print("Please choose how much money you want to add or you want 0 balance account\n"
                      "1. Zero balance\n"
                      "2. Add money\n")
                try:
                    option = int(input())
                    if option == 1:
                        balance = 0
                        break
                    elif option == 2:
                        while True:
                            add = float(input("Enter your amount 200, 500, 1000\n"))
                            if add <=0:
                                print("The amount should be greater than 0 Rs\n")
                                continue
                            elif add<=500:
                                print("The amount should be greater than 500")
                                continue
                            balance = add
                            break
                        break

                    else:
                        print("Enter a valid input\n")
                        continue
                except ValueError:
                    print("Invalid option")
                    continue

            print("Account Created Successfully")
            time.sleep(2)
            print(f"Please Check the detail's \n"
                  f"Name : {account_holder_name}\n"
                  f"Mobile : {mobile_number}\n"
                  f"Pan card : {pan_card}\n"
                  f"Email id : {email_id}\n"
                  f"Balance : {balance}")

        except Exception:
            print(f"")

        confirm = input("To confirm yes press Y for No press N  - ")
        rs = confirm.lower()
        time.sleep(1)
        if rs == "y":
            account_number = random.randint(0, 100000000000) * 10
            feature.account_detail.append(
                Account(account_number, account_holder_name, mobile_number, pan_card, email_id, balance))
            print(f"Note your account number - {account_number}")
            statement_ls.append(BankStatement(account_number, date, balance))
            break
        else:
            print("Re-enter your detail's")
            continue


# Function for account details
def account_detail(account_num):
    for i in feature.account_detail:
        if i.num == account_num:
            print(f"******** Your Account Details **********\n"
                  f"Your name - {i.name}\n"
                  f"Your Mobile - {i.mobile}\n"
                  f"Your Pan Card - {i.pan}\n"
                  f"Your Email - {i.email}\n"
                  f"Bank balance - {i.balance}\n")
            return 0
        else:
            continue
    print(f"No such account found with the number {account_num}\n")
    return None


def animate_text(text):
    while True:
        for i in text:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.2)
        print("\r", end="")
        if input("-") is not None:
            break


# cmd = 'notepad'
# os.system(cmd)
statement_ls = []


class BankStatement:
    def __init__(self,account_num,date, amount):
        self.account_num = account_num
        self.date = date
        self.amount = amount


def cash_add(num):
    try:
        for i in feature.account_detail:
            if i.num == num:
                while True:
                    add = float(input("Enter the amount you want to add\n"))
                    if add <= 0:
                        print("Amount should be greater than 0 Rs\n")
                        continue
                    else:
                        break
                statement_ls.append(BankStatement(num, date, add))
                i.balance += add


                time.sleep(0.5)
                print(f"Amount has been credited successfully your current balance is {i.balance}")
                time.sleep(0.5)
                return
            else:
                continue
        return print(f"No account found with the account num {num}\n")
    except Exception:
        raise exception.fileException.WrongInput(f"Enter a valid amount")


def withdraw(num):
    try:
        for i in feature.account_detail:
            if i.num == num:
                while True:
                    sub = float(input("Enter the amount you want to Withdraw\n"))

                    if i.balance < sub :
                        print(f"You don't have enough money your account balance is {i.num} enter valid amount\n")
                        continue
                    else:
                        break

                if i.balance <= 0:
                    print(f"Your account balance is Too low {i.balance} can't withdraw money")
                    return
                statement_ls.append(BankStatement(num, date, sub))
                i.balance -= sub


                time.sleep(0.5)
                print(f"Amount has been debited successfully your current balance is {i.balance}")
                time.sleep(0.5)
                return
            else:
                continue
        return print(f"No account found with the account num {num}\n")
    except Exception:
        raise exception.fileException.WrongInput(f"Enter a valid amount")


def balance(num):
    for i in feature.account_detail:
        if i.num == num:
            print(f"Your account balance is {i.balance}\n")
            return
        else:
            continue
    return print(f"No account found with the account num {num}\n")


def bank_statement(num):
    for i in feature.account_detail:
        if i.num == num:
            for j in statement_ls:
                if j.account_num == num:
                    print(f"{j.date} \t\t {j.amount}\n")
            return
        else:
            continue
    return print(f"No account found with the account num {num}\n")
