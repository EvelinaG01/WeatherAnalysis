import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Path of csv file C:\Users\user\Desktop
file_path = 'C:/Users/user/Desktop/weather_classification_data.csv' 

# Load csv file to DataFrame
data = pd.read_csv(file_path)

data.head()

# Information about dataset
print(data.info())

# Some statistic information about the numeric variables
print(data.describe())

# Check for missing values in dataset
print(data.isnull().sum())

# number of each value in the column --> 'Temperature'
print(data['Temperature'].value_counts())

# Μean Τemperature
print(data['Temperature'].mean())

# Temperature-Humidity correlation
correlation = data['Temperature'].corr(data['Humidity'])
print(correlation)

# The distribution of temperature
plt.figure(figsize=(10, 6))
sns.histplot(data['Temperature'], bins=30, kde=True, color='red')
plt.title('Κατανομή Θερμοκρασίας')
plt.xlabel('Θερμοκρασία (°C)')
plt.ylabel('Συχνότητα')
plt.grid(True)
plt.show()

# number of each value in the column --> 'Season'
print(data['Season'].value_counts())

# number of each value in the column --> 'Humidity'
print(data['Humidity'].value_counts())

# Categorical variable into numerical
data['Season_numerical'] = pd.factorize(data['Season'])[0]
print(data)
print(data['Season_numerical'])

# Boxplot for Humididty-Season correlation
plt.figure(figsize=(8, 6))
sns.boxplot(x='Season_numerical', y='Humidity', data=data)
plt.title('Κατανομή Υγρασίας ανά Εποχή')
plt.xlabel('Εποχή')
plt.ylabel('Υγρασία')
plt.xticks(ticks=[0, 1, 2, 3], labels=['Winter', 'Spring', 'Summer', 'Autumn'])
plt.grid(True)
plt.tight_layout()
plt.show()
# In[ ]:




