"""
This is my main file where the program start's
"""
from features.NewAccount import account_opening
import features

# Welcome message
object = features.NewAccount.Features()
while True:
    print("Welcome to the ABZ Bank Please select an option")
    print("1. Open Account\n"
          "2. Delete Account\n"
          "3. View Account\n"
          "4. Bank Operation\n")
    chosen_option = int(input("Enter your Option Here - "))
    if chosen_option == 1:
        account_opening()
    elif chosen_option == 2:
        delete = int(input("Enter your account number - \n"))
        object.delete(delete)
    elif chosen_option == 3:
        print("work in progress")
    elif chosen_option == 4:
        print("work in progress")
