# Author: Dan Richmond-Martina

def debt_payment():
    print("\n1: Debt Calculation\n")
    initial_debt = float(input("Enter the amount of your debt: "))
    print("Computed using the formula: initial debt + ((initial_debt + initial_debt) * 2 ** m / 100)")
    while initial_debt < 0:
        # Ensure that a positive number is entered for debt
        print("Please enter a positive number for your debt.")
        initial_debt = float(input("Enter the amount of your debt: "))

    m = 1
    total_payment_owed = initial_debt

    while total_payment_owed < initial_debt * 100:
        total_payment_owed = (initial_debt + initial_debt) * 2 ** m / 100
        print("After " + str(m), "months, you owe a total of: $" + str(initial_debt + total_payment_owed))
        m += 1
