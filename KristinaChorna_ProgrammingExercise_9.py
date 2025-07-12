# Kristina Chorna
# Programming Exercise 9
# The goal of this program is to display information of a bank account including the
# name, account number, amount and interest rate.

# create BankAcct Class
class BankAcct:
    def __init__(self, name, account_number, amount=0.0, interest_rate=0.01):
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate

    def adjust_interest_rate(self, new_rate):
        if new_rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        self.interest_rate = new_rate

    def deposit(self, deposit_amount):
        if deposit_amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.amount += deposit_amount

    def withdraw(self, withdraw_amount):
        if withdraw_amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if withdraw_amount > self.amount:
            raise ValueError("Insufficient funds.")
        self.amount -= withdraw_amount

    def get_balance(self):
        return self.amount

    def calculate_interest(self, days):
        if days < 0:
            raise ValueError("Days cannot be negative.")
        interest = self.amount * self.interest_rate * (days / 365)
        return interest

    def __str__(self):
        interest = self.calculate_interest(30)
        return (f"Account Holder: {self.name}\n"
                f"Account Number: {self.account_number}\n"
                f"Balance: ${self.amount:.2f}\n"
                f"Monthly Interest (30 days): ${interest:.2f}")


def test_bank_acct():
    # Create a bank account
    account = BankAcct("Kristina Chorna", "123455777", 2000.0, 0.03)
    print(account)

    # Deposit money
    print("\nDepositing $500...")
    account.deposit(500)
    print(account)

    # Withdraw money
    print("\nWithdrawing $400...")
    account.withdraw(400)
    print(account)

    # Adjust interest rate
    print("\nAdjusting interest rate to 5%...")
    account.adjust_interest_rate(0.05)
    print(account)

    # Calculate interest for a different number of days
    print("\nCalculating interest for 60 days...")
    interest_60_days = account.calculate_interest(60)
    print(f"Interest for 60 days: ${interest_60_days:.2f}")

    # Display the final account state
    print("\nFinal Account State:")
    print(account)


# Run the test function
if __name__ == "__main__":
    test_bank_acct()
