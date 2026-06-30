import pandas as pd
import numpy as np

df = pd.read_csv('data/superstore.csv', encoding='latin-1')

print(df.shape)          # (9994, 21)
print(df.dtypes)
print(df.isnull().sum())  # check nulls

# Fix date columns
df['Order Date'] = pd.to_datetime(df['Order Date'])

df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# Extract time features
df['Order Year']  = df['Order Date'].dt.year
df['Order Month'] = df['Order Date'].dt.month
df['Order Month Name'] = df['Order Date'].dt.strftime('%b')
df['Ship Days']   = (df['Ship Date'] - df['Order Date']).dt.days

# Flag loss-making orders
df['Is Loss'] = df['Profit'] < 0

# Save cleaned file
df.to_csv('data/superstore_cleaned.csv', index=False)
print("Cleaned dataset saved.")