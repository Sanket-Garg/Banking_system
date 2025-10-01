#sample run 
basic = BasicAccount("Alice", 500)
premium = PremiumAccount("Bob", 1000, 500)

print(basic)
print(premium)

# Deposits & Withdrawals
basic.deposit(200)
basic.withdraw(100)

# Transfer (with PIN verification)
basic.transfer(premium, 50, basic.pin)

# Transaction history
basic.print_statement()
premium.print_statement()

# Overdraft & Premium Features
premium.withdraw(1300)  # uses overdraft
premium.apply_interest(5)  # apply interest
premium.take_loan(500, 10)  # loan with 10% interest
premium.repay_loan(200)

# Card Expiry Check
basic.check_card_expiry()

# Freeze & Unfreeze
basic.freeze_account()
basic.deposit(100)  # should be blocked
basic.unfreeze_account()
basic.deposit(100)

# Monthly fee
premium.deduct_fee(10)

# Close accounts
basic.close_account()
premium.close_account()
