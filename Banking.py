import random  
from datetime import datetime, timedelta


class BasicAccount:
    counter = 0  # Class variable to keep track of the number of accounts

    def __init__(self, ac_name: str, opening_balance: float):
        BasicAccount.counter += 1
        self.name = ac_name
        self.ac_num = f"GB00BANK{BasicAccount.counter:08d}"  # IBAN-like number
        self.balance = opening_balance
        self.card_num = self.generate_card_number()
        self.card_exp = self.generate_card_expiry()
        self.pin = random.randint(1000, 9999)  # card PIN
        self.is_active = True
        self.transactions = []  # Store transaction history

    def __str__(self):
        return (
            f"Account Holder Name: {self.name}\n"
            f"Account Number: {self.ac_num}\n"
            f"Balance: £{self.balance:.2f}\n"
            f"Card Number: {self.card_num}\n"
            f"Card Expiry: {self.card_exp[0]}/{self.card_exp[1]:02d}\n"
            f"PIN: {self.pin}"
        )

    # ------------------ New Features -------------------
    def record_transaction(self, t_type, amount, success=True):
        self.transactions.append({
            "time": datetime.now(),
            "type": t_type,
            "amount": amount,
            "balance": self.balance,
            "status": "Success" if success else "Failed"
        })

    def print_statement(self, n=5):
        print(f"\nMini Statement for {self.name} (Last {n} transactions):")
        for t in self.transactions[-n:]:
            print(f"{t['time']} | {t['type']} | £{t['amount']:.2f} | "
                  f"Bal: £{t['balance']:.2f} | {t['status']}")

    def transfer(self, to_account, amount, pin):
        if not self.verify_pin(pin):  
            print("PIN verification failed. Transfer denied.")
            self.record_transaction("Transfer Out", amount, success=False)
            return
        if self.withdraw(amount):
            to_account.deposit(amount)
            print(f"Transferred £{amount:.2f} to {to_account.get_name()}")
            self.record_transaction("Transfer Out", amount)
            to_account.record_transaction("Transfer In", amount)

    def verify_pin(self, pin):
        return self.pin == pin

    def deduct_fee(self, fee):
        self.balance -= fee
        self.record_transaction("Fee Deduction", fee)
        print(f"Monthly fee of £{fee:.2f} deducted. Balance: £{self.balance:.2f}")

    def freeze_account(self):
        self.is_active = False
        print("Account has been frozen. No transactions allowed.")

    def unfreeze_account(self):
        self.is_active = True
        print("Account has been unfrozen. Transactions allowed.")

    def check_card_expiry(self):
        today = datetime.now()
        expiry_date = datetime(2000 + self.card_exp[1], self.card_exp[0], 1)
        if expiry_date - today < timedelta(days=90):
            print("⚠️ Your card is expiring soon. Please renew.")
        else:
            print("✅ Your card is valid.")

    # ---------------- Existing Features ----------------
    def deposit(self, amount: float):
        if not self.is_active:
            print("Transaction denied. Account is frozen.")
            return
        if amount > 0:
            self.balance += amount
            print(f"Deposited £{amount:.2f}. New balance is £{self.balance:.2f}")
            self.record_transaction("Deposit", amount)
        else:
            print("Invalid deposit amount.")
            self.record_transaction("Deposit", amount, success=False)

    def withdraw(self, amount: float):
        if not self.is_active:
            print("Transaction denied. Account is frozen.")
            return False
        if amount > 0:
            available_balance = self.get_available_balance()
            if amount <= available_balance:
                self.balance -= amount
                print(f"{self.name} has withdrawn £{amount:.2f}. "
                      f"New balance is £{self.balance:.2f}")
                self.record_transaction("Withdrawal", amount)
                return True
            else:
                print(f"Cannot withdraw £{amount:.2f}. Insufficient funds.")
                self.record_transaction("Withdrawal", amount, success=False)
                return False
        else:
            print("Invalid withdrawal amount.")
            self.record_transaction("Withdrawal", amount, success=False)
            return False

    def get_available_balance(self):
        return self.balance

    def get_balance(self):
        return self.balance

    def print_balance(self):
        print(f"Balance: £{self.balance:.2f}")

    def get_name(self):
        return self.name

    def get_ac_num(self):
        return str(self.ac_num)

    def generate_card_number(self):
        return ''.join(str(random.randint(0, 9)) for _ in range(16))

    def generate_card_expiry(self):
        today = datetime.now()
        return (today.month, (today.year + 3) % 100)

    def issue_new_card(self):
        self.card_num = self.generate_card_number()
        self.card_exp = self.generate_card_expiry()

    def close_account(self):
        if self.get_balance() >= 0:
            print(f"Account closed. "
                  f"Amount to be returned: £{self.balance:.2f}.")
            self.withdraw(self.balance)
            return True
        else:
            print("Account can't be closed due to negative balance.")
            return False


class PremiumAccount(BasicAccount):
    def __init__(self, ac_name: str, opening_balance: float, initial_overdraft: float):
        super().__init__(ac_name, opening_balance)
        self.overdraft = True
        self.overdraft_limit = initial_overdraft
        self.loan_balance = 0  # Loan feature

    def __str__(self):
        return (
            super().__str__() +
            f"\nOverdraft Limit: £{self.overdraft_limit:.2f}\n"
            f"Loan Balance: £{self.loan_balance:.2f}"
        )

    def set_overdraft_limit(self, new_limit: float):
        if new_limit >= 0:
            self.overdraft_limit = new_limit
            print(f"Overdraft limit set to £{self.overdraft_limit:.2f}")
        else:
            print("Invalid overdraft limit.")

    def get_available_balance(self):
        return super().get_available_balance() + self.overdraft_limit

    def print_balance(self):
        super().print_balance()
        if self.balance >= 0:
            print(f"Remaining Overdraft: £{self.overdraft_limit:.2f}")
        else:
            remaining_overdraft = max(0, self.overdraft_limit + self.balance)
            print(f"Remaining Overdraft: £{remaining_overdraft:.2f}")

    def close_account(self):
        if self.get_balance() >= 0 and self.loan_balance == 0:
            print(f"Account closed. Amount returned: £{self.balance:.2f}.")
            self.withdraw(self.balance)
            return True
        else:
            print(f"Cannot close account due to "
                  f"overdraft or loan balance £{self.loan_balance:.2f}")
            return False

    # ---------------- Premium Extras ----------------
    def apply_interest(self, rate):
        interest = self.balance * (rate / 100)
        self.balance += interest
        self.record_transaction("Interest", interest)
        print(f"Interest of £{interest:.2f} added. "
              f"New balance: £{self.balance:.2f}")

    def take_loan(self, amount, interest_rate):
        self.loan_balance += amount * (1 + interest_rate / 100)
        self.balance += amount
        self.record_transaction("Loan Taken", amount)
        print(f"Loan of £{amount:.2f} approved at {interest_rate}%. "
              f"Loan balance: £{self.loan_balance:.2f}")

    def repay_loan(self, amount):
        if amount <= self.balance and amount > 0:
            if amount >= self.loan_balance:
                amount = self.loan_balance
            self.balance -= amount
            self.loan_balance -= amount
            self.record_transaction("Loan Repayment", amount)
            print(f"Repaid £{amount:.2f} towards loan. "
                  f"Remaining loan: £{self.loan_balance:.2f}")
        else:
            print("Insufficient balance or invalid repayment amount.")
