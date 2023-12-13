import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Titanic.csv')

df.drop('Cabin', axis=1, inplace=True)

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 12))

sns.scatterplot(x='Fare', y='Sex', data=df, ax=axes[0, 0])
axes[0, 0].set_title('Scatter Plot of Passenger Fare by Gender')

sns.kdeplot(data=df, x='Age', label='Age', ax=axes[0, 1])
axes[0, 1].set_title('Density Distribution of Age')

sns.kdeplot(data=df, x='Fare', label='Fare', ax=axes[1, 0])
axes[1, 0].set_title('Density Distribution of Fare')

class_distribution = df['Pclass'].value_counts()
axes[1, 1].pie(class_distribution, labels=['Class 1', 'Class 2', 'Class 3'], autopct='%1.1f%%', colors=['skyblue', 'lightgreen', 'lightcoral'])
axes[1, 1].set_title('Distribution of Passenger Classes')

plt.show()

survivors_by_class = df.groupby('Pclass')['Survived'].sum()
survival_percentage_by_class = (survivors_by_class / df.groupby('Pclass')['Survived'].count()) * 100

print("Survivors by Class : ",survivors_by_class,"\n")
print("Survival %age by Class : ",survival_percentage_by_class)
