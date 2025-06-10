# Kristina Chorna
# Programming Exercise 3
# The objective of this code is to create a program that asks the user to input their monthly expenses, calculates the
# total, and displays the highest and lowest expenses.

from functools import reduce


def get_expenses():
    expenses = []
    # prompt the user to enter their monthly expenses and the amount for each expense
    print("Please enter your monthly expenses. Type 'done' when you're finished.")

    while True:
        expense_type = input("Enter expense type (or 'done' to finish): ")
        if expense_type.lower() == 'done':
            break
        try:
            amount = float(input(f"Enter amount for {expense_type}: $"))
            expenses.append((expense_type, amount))
        except ValueError:
            print("Please enter a valid number.")

    return expenses


def main():
    expenses = get_expenses()

    if not expenses:
        print("No expenses entered.")
        return

    # calculate the total expenses using reduce
    total = reduce(lambda acc, x: acc + x[1], expenses, 0)

    # calculate the highest and lowest expenses using reduce
    highest = reduce(lambda acc, x: x if x[1] > acc[1] else acc, expenses)

    lowest = reduce(lambda acc, x: x if x[1] < acc[1] else acc, expenses)

    # display the expense summary including the total of the expenses and the highest and lowest expenses
    print("\n--- Monthly Expenses ---")
    print(f"Total Expense: ${total:.2f}")
    print(f"Highest Expense: {highest[0]} - ${highest[1]:.2f}")
    print(f"Lowest Expense: {lowest[0]} - ${lowest[1]:.2f}")


if __name__ == "__main__":
    main()
