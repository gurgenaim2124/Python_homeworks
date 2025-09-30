account_balanace = 2000 
withdrawal_amount = int(input("How much money do you want ? ")) 
current_balance = account_balanace - withdrawal_amount

if account_balanace < withdrawal_amount:
    print(f'"Insufficient funds" current balance: {account_balanace}')
elif account_balanace > withdrawal_amount:
    print(f'"Withdrawal successful" current balance: {current_balance}')