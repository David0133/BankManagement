"""
This is my main file where the program start's
"""
from features.NewAccount import account_opening
import features

# Welcome message
while True:
    try:
        print("Welcome to the ABZ Bank Please select an option")
        print("1. Open Account\n"
              "2. Delete Account\n"
              "3. View Account\n"
              "4. Bank Operation\n"
              "5. Exit\n")
        chosen_option = int(input("Enter your Option Here - "))
        if chosen_option == 1:
            account_opening()
        elif chosen_option == 2:
            delete = int(input("Enter your account number - \n"))
            features.NewAccount.feature.delete(delete)
        elif chosen_option == 3:
            number = int(input("Enter your account number - \n"))
            features.NewAccount.account_detail(number)
        elif chosen_option == 4:
            print("work in progress")
        elif chosen_option == 5:
            print("Thanks for using ABZ bank service")
            break
    except ValueError:
        print("Invalid option please enter a valid response")
