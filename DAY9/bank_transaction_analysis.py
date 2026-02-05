import pandas as pd

transaction_data = {
    'TransactionID': [101, 102, 103, 104, 105, 106],
    'Date': ['2023-11-01', '2023-11-02', '2023-11-03', '2023-11-05', '2023-11-08', '2023-11-10'],
    'Type': ['Deposit', 'Withdrawal', 'Deposit', 'Withdrawal', 'Deposit', 'Withdrawal'],
    'Amount': [5000, 2000, 15000, 500, 50000, 12000]
}

df = pd.DataFrame(transaction_data)

print("--- Original Transactions ---")
print(df)

df['Net_Change'] = df.apply(lambda row: row['Amount'] if row['Type'] == 'Deposit' else -row['Amount'], axis=1)

final_balance = df['Net_Change'].sum()
print(f"\nFinal Account Balance: {final_balance}")

HIGH_VALUE_THRESHOLD = 10000
high_value_transactions = df[df['Amount'] > HIGH_VALUE_THRESHOLD]

print(f"\n--- High Value Transactions (> {HIGH_VALUE_THRESHOLD}) ---")
print(high_value_transactions[['Date', 'Type', 'Amount']])

df['Running_Balance'] = df['Net_Change'].cumsum()
print("\n--- Transaction History with Running Balance ---")
print(df[['Date', 'Type', 'Amount', 'Running_Balance']])


