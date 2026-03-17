#Display summary using head(), tail(), and describe().
import pandas as pd
df = pd.read_csv('student_records.csv')
print("First 5 records:")
print(df.head())
print("\nLast 5 records:")
print(df.tail())
print("\nSummary statistics:")
print(df.describe())
