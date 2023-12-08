
print("Welcome to ADT Banking system.")
details = {"name": "Anaswara Prasad G",
            "Acc_no": 123456789,
            "user_id": "anaswara95",
            "pass_word": 100295,
            "balance":150000
}
recent_credited={"Recent_credited":0}
recent_debited={"Recent_debited":0}
def bank_account():
    print("Please login!")
    userid=(input("Enter your USERID:\t"))
    password=int((input("Enter your PASSWORD:\t")))
    if userid==details["user_id"] and password==details["pass_word"]:
        print("Login successfull!", f"\nWelcome {details["name"]}!")
        return True

    else:
        print("Invalid userid or password.please enter the correct one.")
        reset_password=input("Forgot password?:\t")
        if reset_password == "yes":
            new_password=int(input("Enter your new password:\t"))
            details["pass_word"]=new_password
            print("Password reset successfully!")
            print("Login successfull!", f"\nWelcome {details["name"]}!")
            return True
        else:
            return False
def amount_deposited():
    amount_credited=int(input("\nEnter the amount to be deposited:\t"))
    details["balance"]+=amount_credited
    print(f"Rs.{amount_credited} credited to your account successfully!", f"\nYour current account balance is:\t{details["balance"]}")
    recent_credited["Recent_credited"]=amount_credited
def amount_withdraw():
    amount_debited = int(input("\nEnter the amount to withdraw:\t"))
    if amount_debited<=details["balance"]:
        details["balance"]-=amount_debited
        print(f"Rs.{amount_debited} debited from your account. " f"\nYour current account balance is:\t{details["balance"]}")
        print("If it is not you please call 180057000 ")
        recent_debited["Recent_debited"]=amount_debited

    else:
        print("Insufficient balance!")
from datetime import datetime
current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
def statement():
    print(f"\nStatement generated as of {current_date}")
    recent_time = datetime.now().strftime("%Y-%m-%d")
    monthly_credited = {"2023-11-01 Salary": 80000,
                          "2023-11-01 Interest_on_FD": 5000,
                          f"redited_amount": recent_credited["Recent_credited"]
                          }
    monthly_debited = {"2023-11-05 Rent":10000,
                         "2023-11-06 Grocery":5000,
                         "2023-11-10 Recharge":1000,
                         "2023-11-11 Internet":500,
                         "2023-11-15 Electricity_bill":1200,
                         "2023-11-17 Water_bill":200,
                         "2023-11-{recent_time} C20 Gas_cylinder":1100,
                         f"{recent_time} Debited_amount": recent_debited["Recent_debited"]
    }
    print("Your statement:\t")
    for key, value in monthly_credited.items():
        print(f"{key}: {value}")
    for key, value in monthly_debited.items():
        print(f"{key}: {value}")

    sum_2 = 0
    for value in monthly_credited.values():
        sum_2 += value
    print("Total amount credited to your account :\t", sum_2)

    sum_1 = 0
    for value in monthly_debited.values():
        sum_1 += value
    print("Total amount debited from your account :\t",sum_1)

def options():
    options={"1":amount_deposited,
             "2":amount_withdraw,
             "3": lambda: print(f"Your current account balance is:\t {details["balance"]}"),
             "4":statement
    }

    while True:
        print("\n Options:")
        print("1.Deposite")
        print("2.Withrawal")
        print("3.Balance Inquiry")
        print("4.statement")
        print("5.Exit")

        opt=input("\nChoose the option:\t")
        if opt=="5":
            print("Thank you for using ADT Banking system!")
            break
        elif opt in options:
            options[opt]()
        else:
            print("Invalid option please enter a valid option!")

log_in=bank_account()
if log_in:
    options()
