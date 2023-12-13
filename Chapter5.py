import pandas as pd
import numpy as np
from pandas import Series, DataFrame


#Creation of Series
print("SERIES : ")
print()
print("(1) Creation of Series.")
obj = pd.Series([4, 7, -5, 3])

print()
print("Series : \n",obj)
print("Values of Series : ",obj.values)
print("Indices of Series : ",obj.index)
print()

print("(2) User-Based Indexing of Series.")

obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])

print()
print("Series2 : \n",obj2)
print("Values of Series2 : ",obj2.values)
print("Indices of Series2 : ",obj2.index)
print("Index of User Based Index a :",obj2['a'])
print()

obj2['d'] = 6

print("Series2 after Inserting Element at Index d : \n",obj2)
print("Series with Specific Indices : \n",obj2[['c', 'a', 'd']])
print("Displaying Series2 with Condition : \n", obj2[obj2 > 0])
print("Scalar Multiplication of Series2 : \n",obj2 * 2)
print("Exponential of Series2 : \n", np.exp(obj2))
print()

print("(3) Some More Series Implementations.\n")

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sdata)

print("Series2 : \n",obj3)

states = ['California', 'Ohio', 'Oregon', 'Texas']

obj4 = pd.Series(sdata, index=states)

print("Series4 : \n",obj4)

print("Summation of Series3 & Series4 : \n",obj3 + obj4)

obj4.name = 'population'
obj4.index.name = 'state'

print("Series4 names : \n",obj4)
print()

print("(4) Updating Series1 Indices : \n")

obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']

print("Series1 with Updated Indices : \n",obj)
print()

print("DATAFRAME : ")
print()

data = {'State': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],'Year': [2000, 2001, 2002, 2001, 2002, 2003],'Pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame1 = pd.DataFrame(data)

print("DataFrame1 : \n",frame1 )

print("Implementing head() func : \n", frame1.head())

frame2 =  pd.DataFrame(data, columns=['Year', 'State', 'Pop'])
print("Reordering Columns of DataFrame1 : \n",frame2)
print()

frame3 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],index=['one', 'two', 'three', 'four','five', 'six'])
print("DataFrame3 : \n",frame3)
print()
print("Columns of DataFrame3 : ",frame3.columns)
print()

print("Accessing with Indexing : \n",frame3['state'])
print("Accessing with Attribute : \n",frame3.year)

print("Retrieving Rows with loc() : \n", frame3.loc['three'])

frame3['debt'] = 16.5
print("Inserting a Common Element in Every Rows : \n", frame3)

frame3['debt'] = np.arange(6.)
print("Arranging The Inserted Values : \n",frame3)

val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])

frame3['debt'] = val

print(frame3)

frame3['eastern'] = frame3.state == 'Ohio'

print(frame3)

del frame3['eastern']

print(frame3.columns)

pop = {'Nevada': {2001: 2.4, 2002: 2.9},'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}

frame4 = pd.DataFrame(pop)

print("Dictionary to DataFrame : \n",frame4)
print()
print("Transposing DataFrame4 : \n",frame4.T)

pdata = {'Ohio': frame4['Ohio'][:-1],'Nevada': frame4['Nevada'][:2]}

frame5 = pd.DataFrame(pdata)

print("Slicing The DataFrame : ",frame5)
print()
print("INDEX OBJECTS : ")
print()
indFrame1 = pd.Series(range(3), index=['a', 'b', 'c'])

index = indFrame1.index

print("Indices of New Series : ", index)

print("Slicing Indices : ",index[1:])

labels = pd.Index(np.arange(3))

print("Sharing Index Objects : ",labels)


indFrame2 = pd.Series([1.5, -2.5, 0], index=labels)

print("Index DataFrame2 : \n",indFrame2)

print("Checking for Indices : ", indFrame2.index is labels)

