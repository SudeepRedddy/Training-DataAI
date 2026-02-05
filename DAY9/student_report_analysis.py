import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('student_report.csv')

print("\n--- Original Data ---")
print(df)

print("\n--- Missing Values Count ---")
print(df.isnull().sum())

df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Marks'] = df['Marks'].fillna(df['Marks'].mean())

df['City'] = df['City'].str.strip().str.title()

print("\n--- Cleaned Data ---")
print(df)


avg_marks = df['Marks'].mean()
print(f"\nAverage Marks: {avg_marks:.2f}")

top_student_idx = df['Marks'].idxmax()
top_student = df.loc[top_student_idx]
print(f"Top Scoring Student: {top_student['Name']} with {top_student['Marks']} marks")

low_scorers = df[df['Marks'] < 70]
print("\n--- Students Scoring Below 70 ---")
print(low_scorers[['Name', 'Marks', 'Class']])


plt.figure(figsize=(8, 5))
plt.bar(df['Name'], df['Marks'], color='skyblue', edgecolor='black')

plt.xlabel('Student Name')
plt.ylabel('Marks')
plt.title('Student Marks Distribution')
plt.axhline(y=avg_marks, color='r', linestyle='--', label=f'Average ({avg_marks:.1f})')
plt.legend()
plt.show()