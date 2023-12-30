"""
This is my main file where the program start's
"""
from features.NewAccount import account_opening
import exception.fileException
import features
from schedule import repeat, every
from matplotlib import pyplot as plt

# Welcome message
print("Welcome to the ABZ Bank Please select an option")

features.NewAccount.animate_text("Press any key to Enter")
while True:
    try:
        try:
            print("1. Open Account\n"
                  "2. Delete Account\n"
                  "3. View Account\n"
                  "4. Bank Operation\n"
                  "5. Exit\n")
            chosen_option = int(input("Choose your option - "))
            if chosen_option == 1:
                account_opening()
            elif chosen_option == 2:
                delete = int(input("Enter your account number - \n"))
                features.NewAccount.feature.delete(delete)
            elif chosen_option == 3:
                number = int(input("Enter your account number - \n"))
                features.NewAccount.account_detail(number)
            elif chosen_option == 4:
                print("1. Add Cash\n"
                      "2. Withdraw Cash\n"
                      "3. Balance check\n"
                      "4. Statement\n")
                user_choice = int(input("Your choice - "))
                if user_choice == 1:
                    account_number = int(input("Enter your Account Number\n"))
                    features.NewAccount.cash_add(account_number)
                elif user_choice == 2:
                    account_number = 0
                    while True:
                        try:
                            account_number = int(input("Enter your Account Number\n"))
                        except:
                            raise exception.fileException.WrongInput("Enter a valid Account number")
                        break

                    features.NewAccount.withdraw(account_number)
                elif user_choice == 3:
                    account_number = int(input("Enter your Account Number\n"))
                    features.NewAccount.balance(account_number)
                elif user_choice == 4:
                    account_number = int(input("Enter your Account Number\n"))
                    features.NewAccount.bank_statement(account_number)

            elif chosen_option == 5:
                print("Thanks for using ABZ bank service")
                break
        except ValueError:
            raise exception.fileException.WrongInput("Choose a valid option")
    except Exception as e:
        print(f"Warning! {e}")
