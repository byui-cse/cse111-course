"""
CSE 111
Lesson 06 ICE - Debugging functions
Author: [Your Name Here]

Description:
Practice debugging functions by fixing the code below.

You may add additional print statements and/or use the
debugger to help you.

Instructions:
    1. Fix the code below so it correctly calculates the monthly payment
       on a loan.

    2. (Stretch) Add a second function named "compute_total_payment"
       that multiplies the monthly payment by the total number of months
       to show how much the user will pay in total over the life of the
       loan.

    3. (Stretch) Write a test function in a separate file to test your
       computer_monthly_payment and compute_total_payment functions
       using pytest.

Notes:
Use the website https://www.calculator.net/amortization-calculator.html
to check your calculations.

The forumal to calculate the monthly payment on a loan is:

           P * r
    M = -------------
                  -n
         1 - (1+r)

where
    M  Monthly payment you will owe
    P  Principal - the amount borrowed
    r  Periodic interest rate - the annual rate divided by 12
    n  Total number of payments - the number of years times 12
"""

def main():
    principal = float(input("Enter the loan amount: "))
    rate = float(input("Enter the annual rate (as a decimal, e.g., 0.06): "))
    years = int(input("How many years is the loan for? "))

    monthly_payment = compute_monthly_payment(principal, rate, years)
    print(f"Monthly payment is: {monthly_payment:.2f}")

    total_payment = compute_total_payment(monthly_payment, years)
    print(f"Total paid over the life of the loan: {total_payment:.2f}.")


def compute_monthly_payment(p, r, y):
    if p == 0: # loan amount is 0
        return 0

    if y == 0: # Length of loan is 0
        return p

    if r == 0: # interest rate is 0
        return p / (y * 12)

    months = y * 12
    monthly_rate = r / 12
    return p * monthly_rate / (1 - (1 + monthly_rate) ** -months)


def compute_total_payment(monthly_payment, years):
    return monthly_payment * 12 * years


if __name__ == "__main__":
    main()
