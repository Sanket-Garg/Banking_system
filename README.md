This project implements a banking system simulator in Python with two types of accounts:

Basic Account

Premium Account (with overdraft and loan features)

It allows users to perform common banking operations such as deposits, withdrawals, transfers, and also introduces real-world features like overdrafts, loans, transaction history, card expiry checks, and account freezing.

✨ Features
🔹 Basic Account

Open an account with an initial balance

Deposit & withdraw money

Transfer money to another account (with PIN verification)

Transaction history (mini statement)

Account number generation (IBAN-like format)

Debit card generation with expiry date

Card renewal reminders

Account freeze/unfreeze for security

Monthly maintenance fees

Close account (if balance ≥ 0)

🔹 Premium Account (inherits from BasicAccount)

All features of BasicAccount

Overdraft facility with configurable limit

Loan borrowing and repayment with interest

Interest applied on account balance

Remaining overdraft tracking

Cannot close account if loan or overdraft outstanding
