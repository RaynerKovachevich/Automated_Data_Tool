import pandas as pd
import matplotlib.pyplot  as plt
import seaborn as sns

#load csv file
filename = input("Enter the csv file name (with .csx extension):")
df = pd.read_csv('your_data.csv')

#view the first few rows
print("Original Data:")
print(df.head())

#Drop rows with missing data
df_cleaned = df.dropna()

#Rename columns (optional)
df_cleaned.columns = ['columns1', 'columns2', 'columns3', 'columns4']

filterd_data = df_cleaned[df_cleaned['columns1'] > 10]

#Calculate the average of a column
avg_value = filterd_data["columns1"].mean()
print('Average value:', avg_value)

filterd_data['column_calculated'] = filterd_data['columns1']

filterd_data.to_csv('processed_data.csv', index=False)
filterd_data.to_excel('processed_data.xlsx', index=False)

plt.figure(figsize=(10, 6))
sns.barplot(x="columns1", y='column_calculated', data=filterd_data)
plt.title('sample Bar Plot of Filtered Data')
plt.xlabel('columns1')
plt.ylabel('Calculated Column')
plt.show()