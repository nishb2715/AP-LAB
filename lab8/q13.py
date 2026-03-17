#Create a bar chart of student marks.
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('student_records.csv')
plt.bar(df['Name'], df['Marks'], color='blue')
plt.xlabel('Student Name')
plt.ylabel('Marks')
plt.title('Student Marks Bar Chart')
plt.show()
