#Replace missing values with mean.
import pandas as pd
df = pd.read_csv('student_records.csv')
df.fillna(df.mean(), inplace=True)
print("Data after replacing missing values with mean:")
print(df)
