import pandas as pd

#(A)
df1 = pd.read_excel('workshop1.xlsx')
df2 = pd.read_excel('workshop2.xlsx')

common_attendees = pd.merge(df1, df2, on=['Name', 'Date', 'duration'])

print(common_attendees['Name'])


#(B)
single_attendees = pd.merge(df1, df2, on=['Name', 'Date', 'duration'], how='outer', indicator=True)

single_workshop_only = single_attendees[single_attendees['_merge'] == 'left_only']

print(single_workshop_only['Name'])


#(C)
merged_df = pd.concat([df1, df2])

total_records = len(merged_df)

print("Total Number of Records:", total_records)


#(D)
merged_df = pd.concat([df1, df2]).set_index(['Name', 'Date'])

print(merged_df)

#Descriptive Stats
stats = merged_df.describe()

print(stats)
