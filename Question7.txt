import pandas as pd

data = {'FamilyName': ['Shah', 'Vats', 'Vats', 'Kumar', 'Vats', 'Kumar', 'Shah', 'Shah', 'Kumar', 'Vats'],
        'Gender': ['Male', 'Male', 'Female', 'Female', 'Female', 'Male', 'Male', 'Female', 'Female', 'Male'],
        'MonthlyIncome': [44000.00, 65000.00, 43150.00, 66500.00, 255000.00, 103000.00, 55000.00, 112400.00, 81030.00, 71900.00]}

df = pd.DataFrame(data)

# a. Calculate and display familywise gross monthly income.
familywise_gross = df.groupby('FamilyName')['MonthlyIncome'].sum()
print()
print("a. Familywise Gross Monthly Income : ")
print(familywise_gross)
print()

# b. Display the highest and lowest monthly income for each family name.
highest_income = df.groupby('FamilyName')['MonthlyIncome'].max()
lowest_income = df.groupby('FamilyName')['MonthlyIncome'].min()
print("b. Highest Monthly Income : ")
print(highest_income)
print()
print("Lowest Monthly Income : ")
print(lowest_income)
print()

# c. Calculate and display monthly income of all members earning less than Rs. 80000.00.
income_below_80000 = df[df['MonthlyIncome'] < 80000.00]
print("c. Monthly Income of Members Earning Less than Rs. 80000.00:")
print(income_below_80000[['FamilyName', 'MonthlyIncome']])
print()

# d. Display total number of females along with their average monthly income.
female_data = df[df['Gender'] == 'Female']
total_females = female_data.shape[0]
average_income_female = female_data['MonthlyIncome'].mean()
print("d. Total Number of Females and Their Average Monthly Income : ")
print(f"Total Females : {total_females}")
print(f"Average Monthly Income of Females : {average_income_female:.2f}")
print()

# e. Delete rows with Monthly income less than the average income of all members.
average_income_all = df['MonthlyIncome'].mean()
df = df[df['MonthlyIncome'] >= average_income_all]
print("e. DataFrame after deleting rows with Monthly income less than the average income : ")
print(df)
