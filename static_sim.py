bank_balance = 0.0

# Create three accounts initialized to different balances
account_a = 10.0
account_b = 0.0
account_c = 10.0

# Print opening balances
print(f"{account_a}\t{account_b}\t{account_c}\t{bank_balance}")

# Process ten cycles
for i in range(10):
    # Calculate average balance
    average_balance = (account_a + account_b + account_c) / 3

    # For each account, if balance is above average, transfer one coin to bank
    if account_a > average_balance:
        account_a -= 1
        bank_balance += 1
    if account_b > average_balance:
        account_b -= 1
        bank_balance += 1
    if account_c > average_balance:
        account_c -= 1
        bank_balance += 1

    print(f"{account_a}\t{account_b}\t{account_c}\t{bank_balance}")
    
    # For each account, if balance is below average, transfer one coin from bank
    if account_a < average_balance:
        account_a += 1
        bank_balance -= 1
    if account_b < average_balance:
        account_b += 1
        bank_balance -= 1
    if account_c < average_balance:
        account_c += 1
        bank_balance -= 1

    print(f"{account_a}\t{account_b}\t{account_c}\t{bank_balance}")
