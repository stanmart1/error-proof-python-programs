import math

# Payment formulas:
# monthly payment = principal/months
# no of monthly payments = principal/payments
# last_payment = principal - (periods - 1) * payment

# If the last payment differs from the rest,
# the program should display the monthly payment
# and the last payment.


# function to calculate monthly payments
def monthly_payment(principal_, months_):
    monthly_ = principal_/months_
    if monthly_ % 2 != 0:
        monthly_ = math.ceil(monthly_)
        last_payment = principal_ - (months_ - 1) * monthly_
        monthly_ = round(monthly_)
        print(f"Your monthly payment = {monthly_} and the last payment = {last_payment}.")
    else:
        monthly_ = round(monthly_)
        print(f"Your monthly payment = {monthly_}")


# function to calculate number of months to repay loan
def no_of_months(principal_, monthly_):
    months_ = principal_/monthly_
    if months_ % 2 != 0:
        months_ = round(months_)
    if months_ > 1:
        print(f"It will take {months_} months to repay the loan")
    else:
        print(f"it will take {months_} month to repay the loan")


# write your code here
principal = 0
monthly = 1
months = 1
print("Enter the loan principal:")
while True:
    try:
        principal = int(input())
        if principal > 1:
            break
        else:
            print("Principal must be greater than 1")
            continue
    except ValueError:
        print("loan principal must be in digits")
        continue

print('What do you want to calculate?\ntype "m" for number of monthly payments,\ntype "p" for the monthly payment:')
while True:
    user_ans = input()
    if user_ans == 'm':
        print("Enter the monthly payment:")
        while True:
            try:
                monthly = int(input())
                if monthly > 0:
                    break
                else:
                    print("Monthly payment must be greater than zero")
                    continue
            except ValueError:
                print("monthly payment must be in digits")
                continue

        # call the number of months function
        no_of_months(principal, monthly)
        break
    elif user_ans == 'p':
        print("Enter the number of months:")
        while True:
            try:
                months = int(input())
                if months > 0:
                    break
                else:
                    print("number of months must be greater than zero")
                    continue
            except ValueError:
                print("number of months must be in digits")
                continue

        # call the monthly payments function
        monthly_payment(principal, months)
        break
    else:
        print('Choose between "m" or "p"')
        continue
