def account_opening():
    account_holder_name = str(input("Enter Your good name\n"))
    mobile_number = int(input("Enter your mobile number\n"))
    pan_card = int(input("Enter Pan card Number\n"))
    email_id = list(input("Your email id\n"))

    print(f"Check the details to confirm \n"
          f"Name : {account_holder_name}\n"
          f"Mobile : {mobile_number}\n"
          f"Pan card : {pan_card}\n"
          f"Email id : {email_id}\n")


