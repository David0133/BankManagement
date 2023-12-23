"""
This is my main file where the program start's
"""
from features.NewAccount import account_opening
# Welcome message
print("Welcome to the ABZ Bank Please select an option")
print("1. Open Account\n"
      "2. Delete Account\n"
      "3. View Account\n"
      "4. Bank Operation\n")
choosen_option = int(input("Enter your Option Here - "))
if choosen_option == 1:
    account_opening()

