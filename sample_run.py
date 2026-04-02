from Banking import BasicAccount, PremiumAccount, FraudMonitor


def separator(title=""):
    print("\n" + "=" * 55)
    if title:
        print(f"  {title}")
        print("=" * 55)


# ── ACCOUNT CREATION ──────────────────────────────────────
separator("ACCOUNT CREATION")

basic = BasicAccount("Alice", 500)
premium = PremiumAccount("Bob", 1000, 500)

print(basic)
print()
print(premium)


# ── STANDARD OPERATIONS ───────────────────────────────────
separator("DEPOSITS & WITHDRAWALS")

basic.deposit(200)
basic.withdraw(100)


# ── TRANSFER WITH PIN VERIFICATION ────────────────────────
separator("TRANSFER — PIN VERIFICATION")

basic.transfer(premium, 50, basic.pin)
basic.transfer(premium, 50, 0000)        # deliberate wrong PIN


# ── PREMIUM FEATURES ──────────────────────────────────────
separator("PREMIUM ACCOUNT — OVERDRAFT, LOAN, INTEREST")

premium.withdraw(1300)                   # uses overdraft
premium.print_balance()
premium.apply_interest(5)
premium.take_loan(500, 10)
premium.repay_loan(200)


# ── CARD OPERATIONS ───────────────────────────────────────
separator("CARD EXPIRY & REISSUE")

basic.check_card_expiry()
basic.issue_new_card()
basic.check_card_expiry()


# ── FREEZE / UNFREEZE ─────────────────────────────────────
separator("ACCOUNT FREEZE & UNFREEZE")

basic.freeze_account()
basic.deposit(100)                       # blocked
basic.withdraw(50)                       # blocked
basic.unfreeze_account()
basic.deposit(100)                       # allowed


# ── MONTHLY FEE ───────────────────────────────────────────
separator("FEE DEDUCTION")

premium.deduct_fee(10)


# ── TRANSACTION STATEMENTS ────────────────────────────────
separator("MINI STATEMENTS")

basic.print_statement(n=10)
premium.print_statement(n=10)


# ── AML SUSPICIOUS ACTIVITY SIMULATION ───────────────────
separator("AML SIMULATION — SUSPICIOUS ACCOUNTS")

# Suspect 1: high frequency withdrawals (velocity flag)
suspect1 = BasicAccount("James Moriarty", 5000)
print("\nSimulating high-frequency outflows on suspect1...")
for amount in [150, 200, 180, 160, 140]:
    suspect1.withdraw(amount)

# Suspect 2: structuring / smurfing pattern
suspect2 = PremiumAccount("Irene Adler", 10000, 2000)
print("\nSimulating structuring pattern on suspect2...")
suspect2.withdraw(490)
suspect2.withdraw(480)
suspect2.withdraw(470)

# Suspect 3: single high-value transaction
suspect3 = BasicAccount("Sebastian Moran", 8000)
print("\nSimulating high-value transaction on suspect3...")
suspect3.withdraw(600)

# Clean account — should pass screening
clean = BasicAccount("John Watson", 3000)
clean.deposit(500)
clean.withdraw(100)


# ── AML PORTFOLIO SCREENING ───────────────────────────────
separator("AML PORTFOLIO SCREENING — FRAUD MONITOR")

monitor = FraudMonitor()
monitor.register_account(suspect1)
monitor.register_account(suspect2)
monitor.register_account(suspect3)
monitor.register_account(clean)
monitor.register_account(basic)
monitor.register_account(premium)

monitor.run_screening(
    window_minutes=60,
    max_transactions=5,
    amount_threshold=500
)


# ── INDIVIDUAL AML REPORTS ────────────────────────────────
separator("INDIVIDUAL AML REPORTS")

suspect1.aml_report()
suspect2.aml_report()
suspect3.aml_report()
clean.aml_report()


# ── ALERT EXPORT ──────────────────────────────────────────
separator("ALERT LOG EXPORT")

monitor.export_alert_log("aml_alerts.csv")
monitor.summary_report()


# ── ACCOUNT CLOSURE ───────────────────────────────────────
separator("ACCOUNT CLOSURE")

basic.close_account()
premium.close_account()          # blocked — outstanding loan
premium.repay_loan(premium.loan_balance)
premium.close_account()          # now succeeds


separator("DEMO COMPLETE")
```
