#Compute a correlation matrix using pandas.
import pandas as pd
df = pd.read_csv('student_records.csv')
correlation_matrix = df.corr()
print("Correlation Matrix:")
print(correlation_matrix)

