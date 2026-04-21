# Banking System with AML Transaction Monitoring

## Overview
A modular Python banking system simulating core retail banking operations 
with a built-in Anti-Money Laundering (AML) monitoring layer.

Built to demonstrate understanding of financial crime typologies and 
compliance workflows alongside OOP design principles.

## Features

### Core Banking
- Account creation with auto-generated UK-format account numbers
- Deposits, withdrawals, transfers with PIN verification  
- Card issuance and expiry management
- Account freezing/unfreezing
- Premium accounts with overdraft and loan facilities

### AML Monitoring (Key Feature)
Three detection typologies implemented:

| Typology | Logic |
|---|---|
| High Frequency | >5 outflows within 60-minute rolling window |
| High Value | Single transaction exceeding £500 threshold |
| Structuring/Smurfing | 3+ sub-threshold transactions summing above threshold |

### FraudMonitor Class
Portfolio-level screening across all accounts — mimics a basic 
Financial Intelligence Unit (FIU) system:
- Screens all registered accounts simultaneously
- Auto-freezes accounts on positive alert
- Exports alert log to CSV for Power BI dashboard reporting

## Technical Stack
- Python 3.x
- OOP with inheritance (BasicAccount → PremiumAccount)
- CSV export compatible with Power BI
- datetime-based rolling window logic

## Project Structure
banking_system/
├── banking_system.py   # Core classes
├── demo.py             # Full working demonstration  
├── test_banking.py     # Unit tests
├── aml_alerts.csv      # Sample output
└── README.md

## AML Concepts Referenced
- Velocity monitoring
- Structuring / smurfing detection
- Suspicious Activity Report (SAR) workflow simulation
- Account freezing on alert (regulatory hold simulation)

## How to Run
python demo.py

## Sample Output
[Screenshot here]
