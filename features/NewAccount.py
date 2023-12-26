import random


class Features:
    account_detail = []


    def append(self,item):
        self.account_detail.append(item)

    def delete(self,num):
        if self.account_detail.__contains__(num):
            self.account_detail.remove(num)
            print("Account deleted successfully")
        else:
            print("No account found please check your account number")


#making class object
feature = Features()

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
            feature.append(account_number)
            print(f"Note your account number - {account_number}")

            break
        else:
            print("Re-enter your detail's")
            continue

def delete_account(account_num):
    feature.delete(account_num)




