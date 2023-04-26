import math

# A = annuity
# P = loan principal
# i = nominal (monthly) interest rate. usually, it is 1/12 of the
# annual interest rate. It is a floating value, not a percentage.
# i = (12/100) * annual_interest_rate
# n = number_of_payments. This is usually the number of months in which
#     repayments will be made.
#
#
# annuity (A)           = p * i * (1 + i)**n / ((1 + i)**n - 1)
# principal (P)         = A / (i * (1 + i)**n / ((1 + i)**n - 1))
# alternate (P)         = (A * ((1 + i) ** n - 1)) / i
# number of payments(n) = math.log(A / (A - P * i)) / math.log(1 + i)


# Payment formulas:
# monthly payment = principal/months
# no of monthly payments = principal/payments
# last_payment = principal - (periods - 1) * payment


def nominal_interest(num_int):
    return (1/12) * num_int/100


def principal_p(a, i, n):
    i = nominal_interest(i)
    loan_principal = a / (i * (1 + i)**n / ((1 + i)**n - 1))
    loan_principal = math.floor(loan_principal)
    print(f"Your loan principal = {loan_principal}!")


def annuity_a(p, i, n):
    i_monthly = nominal_interest(i)
    annuity_l = p * (i_monthly * (1 + i_monthly) ** n) / ((1 + i_monthly) ** n - 1)
    annuity_l = math.ceil(annuity_l)
    print(f"Your monthly payment = {annuity_l}!")


def num_of_payments_n(a, p, i):
    i = nominal_interest(i)
    return math.ceil(math.log(a / (a - i * p), 1 + i))


# code section
print("""What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:""")
principal = 1000
periods = 1
loan_interest = 0.1
monthly_interest = 0.1
monthly = 1

while True:
    user_ans = input()
    if user_ans == "a":
        while True:
            print("Enter the loan principal:")
            try:
                principal = int(input())
                if principal >= 1000:
                    break
                else:
                    print("Principal cannot be less than 1000")
                    continue
            except ValueError:
                print("principal must be in digits without commas")
                continue
            except TypeError:
                print("Principal must be a whole number")
                continue
        while True:
            try:
                print("Enter the number of periods:")
                periods = int(input())
                if periods >= 1:
                    break
                else:
                    print("periods must be greater than or equal to 1")
                    continue
            except ValueError:
                print("Periods must be in digits without commas")
                continue
            except TypeError:
                print("Periods must be a whole number")
                continue
        while True:
            try:
                print("Enter the loan interest:")
                loan_interest = float(input())
                if loan_interest > 0:
                    break
                else:
                    print("loan interest must be greater than zero")
                    continue
            except ValueError:
                print("Loan interest must be in digits")
                continue

        # call the annuity/monthly payments function
        annuity_a(principal, loan_interest, periods)
        break
    if user_ans == "n":
        while True:
            print("Enter the loan principal:")
            try:
                principal = int(input())
                if principal >= 10:
                    break
                else:
                    print("Principal cannot be less than 10")
                    continue
            except ValueError:
                print("principal must be in digits without commas")
                continue
            except TypeError:
                print("Principal must be a whole number")
                continue
        while True:
            try:
                print("Enter the monthly payment:")
                monthly = int(input())
                if monthly >= 1:
                    break
                else:
                    print("monthly payment must be greater than or equal to 1")
                    continue
            except ValueError:
                print("monthly payment must be in digits without commas")
                continue
            except TypeError:
                print("monthly payment must be a whole number")
                continue
        while True:
            try:
                print("Enter the loan interest:")
                loan_interest = float(input())
                if loan_interest > 0:
                    break
                else:
                    print("loan interest must be greater than zero")
                    continue
            except ValueError:
                print("Loan interest must be in digits")
                continue
        # call the number of months function and store return value in number_of_monthly_payments variable
        number_of_monthly_payments = num_of_payments_n(monthly, principal, loan_interest)
        if number_of_monthly_payments <= 12:
            print(f"It will take {number_of_monthly_payments} months to repay this loan!")
        if number_of_monthly_payments > 12:
            years_to_repay = number_of_monthly_payments / 12
            years_to_repay = math.floor(years_to_repay)  # round down years to repay
            months_to_repay = number_of_monthly_payments % 12
            if years_to_repay == 1 and months_to_repay == 1:
                print(f"It will take {years_to_repay} year and {months_to_repay} month to repay this loan!")
            if years_to_repay > 1 and months_to_repay == 1:
                print(f"It will take {years_to_repay} years and {months_to_repay} month to repay this loan!")
            if years_to_repay > 1 and months_to_repay > 1:
                print(f"It will take {years_to_repay} years and {months_to_repay} months to repay this loan!")
            if years_to_repay > 1 and months_to_repay == 0:
                print(f"It will take {years_to_repay} years to repay this loan!")
        break
    if user_ans == "p":
        while True:
            print("Enter the annuity payment:")
            try:
                monthly = float(input())
                if monthly >= 0:
                    break
                else:
                    print("annuity cannot be less than 1")
                    continue
            except ValueError:
                print("annuity must be in digits without commas")
                continue
        while True:
            try:
                print("Enter the number of periods:")
                periods = int(input())
                if periods >= 1:
                    break
                else:
                    print("periods must be greater than or equal to 1")
                    continue
            except ValueError:
                print("Periods must be in digits without commas")
                continue
            except TypeError:
                print("Periods must be a whole number")
                continue
        while True:
            try:
                print("Enter the loan interest:")
                loan_interest = float(input())
                if loan_interest >= 0:
                    break
                else:
                    print("loan interest cannot be less than")
                    continue
            except ValueError:
                print("Loan interest must be in digits")
                continue
        principal_p(monthly, loan_interest, periods)
        break
    else:
        print("Invalid Entry")
        print('type "n" for number of monthly payments,\n'
              'type "a" for annuity monthly payment amount,\n'
              'type "p" for loan principal:')
        continue
