#Filter rows based on a condition (marks > 60).
import pandas as pd
df = pd.read_csv('student_records.csv')
filtered_df = df[df['Marks'] > 60]
print("Students with marks greater than 60:")
print(filtered_df)

