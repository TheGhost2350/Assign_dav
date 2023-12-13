import numpy as np
import pandas as pd
import sys
import csv

# Reading CSV into DataFrame with Default Delimiter (Comma)
df = pd.read_csv('examples/ex1.csv')

# Reading CSV with Specified Delimiter (Comma)
df = pd.read_table('examples/ex1.csv', sep=',')
print(df,"\n")

# Reading CSV without Header and Specifying Column Names
df_no_header = pd.read_csv('examples/ex2.csv', header=None)
print(df_no_header,"\n")

df_specify_names = pd.read_csv('examples/ex2.csv', names=['a', 'b', 'c', 'd', 'message'])
print(df_specify_names,"\n")

# Specifying Index Column in CSV
names = ['a', 'b', 'c', 'd', 'message']
df_index = pd.read_csv('examples/ex2.csv', names=names, index_col='message')
print(df_index,"\n")

# Hierarchical Index from Multiple Columns
parsed = pd.read_csv('examples/csv_mindex.csv', index_col=['key1', 'key2'])
print(parsed,"\n")

# Reading CSV with Variable Whitespace (Using Regular Expression)
result = pd.read_table('examples/ex3.txt', sep='\s+')
print(result,"\n")

# Skipping Rows in CSV
df_skip_rows = pd.read_csv('examples/ex4.csv', skiprows=[0, 2, 3])
print(df_skip_rows,"\n")

# Handling Missing Values in CSV
result_missing_values = pd.read_csv('examples/ex5.csv', na_values=['NULL'])
print(result_missing_values,"\n")

# Specifying Different NA Sentinels for Each Column
sentinels = {'message': ['foo', 'NA'], 'something': ['two']}
df_custom_na = pd.read_csv('examples/ex5.csv', na_values=sentinels)
print(df_custom_na,"\n")

# Set the display max rows option
pd.options.display.max_rows = 10

# Read a small number of rows or specify chunksize while reading a large CSV file ex6.csv
result_small_rows = pd.read_csv('examples/ex6.csv', nrows=5)
print(result_small_rows,"\n")

chunker = pd.read_csv('examples/ex6.csv', chunksize=1000)
print(chunker,"\n")

# Iterate over chunks and aggregate value counts in the 'key' column
tot = pd.Series([])
for piece in chunker:
    tot = tot.add(piece['key'].value_counts(), fill_value=0)
tot = tot.sort_values(ascending=False)
print(tot[:10],"\n")

# Write DataFrame data to a CSV file
data = pd.read_csv('examples/ex5.csv')
print(data,"\n")

print(data.to_csv('examples/out.csv', index=False))
print()

# Write DataFrame data to a CSV file with different delimiters and handling missing values
print(data.to_csv(sys.stdout, sep='|'))
print()
print(data.to_csv(sys.stdout, na_rep='NULL'))
print()

# Write a subset of columns to a CSV file
print(data.to_csv(sys.stdout, index=False, header=False))
print()
print(data.to_csv(sys.stdout, index=False, columns=['a', 'b', 'c']))
print()

# Write a Series to a CSV file
ts = pd.Series(np.arange(7), index=pd.date_range('1/1/2000', periods=7))
print(ts.to_csv('examples/tseries.csv'))
print()

# Read a CSV file ex7.csv using Python's csv module for more manual processing
with open('examples/ex7.csv') as f:
    lines = list(csv.reader(f))
header, values = lines[0], lines[1:]
data_dict = {h: v for h, v in zip(header, zip(*values))}
print(data_dict,"\n")

#Reading Microsoft Excel Files

xlsx = pd.ExcelFile('examples/ex1.xlsx')
print(pd.read_excel(xlsx, 'Sheet1'))
print()

frame = pd.read_excel('examples/ex1.xlsx', 'Sheet1')
print(frame, "\n")

# writer = pd.ExcelWriter('examples/ex2.xlsx')
# frame.to_excel(writer, 'Sheet1')
# writer.save()
# frame.to_excel('examples/ex2.xlsx')

with pd.ExcelWriter('examples/ex2.xlsx') as writer:
    frame.to_excel(writer, 'Sheet1')