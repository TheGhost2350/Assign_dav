import pandas as pd, numpy as np
from numpy import nan as NA

string_data = pd.Series(['aardvark', 'artichoke', np.nan, 'avocado'])

print(string_data)
print()
print( string_data.isnull())
print()

string_data[0] = None

print()
print( string_data.isnull())
print()

data = pd.Series([1, NA, 3.5, NA, 7])
print(data.dropna())
print()
print(data[data.notnull()])

data = pd.DataFrame([[1., 6.5, 3.], [1., NA, NA],[NA, NA, NA], [NA, 6.5, 3.]])

cleaned = data.dropna()

print()
print(data)
print()
print(cleaned)

print(data.dropna(how='all'))

data[4] = NA

print()
print(data)
print()
print( data.dropna(axis=1, how='all'))
print()

df = pd.DataFrame(np.random.randn(7, 3))
df.iloc[:4, 1] = NA
df.iloc[:2, 2] = NA

print(df)
print()
print(df.dropna())
print()
print(df.fillna(0))
print()
print(df.fillna({1: 0.5, 2: 0}))
_ = df.fillna(0, inplace=True)
print()
print(df)

df = pd.DataFrame(np.random.randn(6, 3))
df.iloc[2:, 1] = NA
df.iloc[4:, 2] = NA

print()
print(df)
print()
print(df.fillna(method='ffill'))
print()
print(df.fillna(method='ffill', limit=2))
print()

data = pd.Series([1., NA, 3.5, NA, 7])
print(data.fillna(data.mean()))
print()

data = pd.DataFrame({'k1': ['one', 'two'] * 3 + ['two'],'k2': [1, 1, 2, 3, 3, 4, 4]})
print(data)
print()
print(data.drop_duplicates())
print()

data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon','Pastrami', 'corned beef', 'Bacon','pastrami', 'honey ham', 'nova lox'],'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
print(data)
print()

meat_to_animal = {'bacon': 'pig','pulled pork': 'pig','pastrami': 'cow','corned beef': 'cow','honey ham': 'pig','nova lox': 'salmon'}

lowercased = data['food'].str.lower()
print(lowercased)
print()

data['animal'] = lowercased.map(meat_to_animal)
print(data)
print()


data = pd.Series([1., -999., 2., -999., -1000., 3.])
print(data.replace(-999, np.nan))
print()
print(data.replace([-999, -1000], np.nan))

data = pd.DataFrame(np.arange(12).reshape((3, 4)),index=['Ohio', 'Colorado', 'New York'],columns=['one', 'two', 'three', 'four'])


transform = lambda x: x[:4].upper()
print()
print(data.index.map(transform))

data.index = data.index.map(transform)
print()
print(data)
print()
print(data.rename(index={'OHIO': 'INDIANA'},columns={'three': 'peekaboo'}))
print()

data = np.random.rand(20)

print(pd.cut(data, 4, precision=2))


data = pd.DataFrame(np.random.randn(1000, 4))
print()
print(data.describe())

col = data[2]
print()
print(col[np.abs(col) > 3])


df = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],'data1': range(6)})
print()
print(pd.get_dummies(df['key']))

dummies = pd.get_dummies(df['key'], prefix='key')
df_with_dummy = df[['data1']].join(dummies)
print()
print(df_with_dummy)

np.random.seed(12345)
values = np.random.rand(10)
print()
print(values)


bins = [0, 0.2, 0.4, 0.6, 0.8, 1]

print(pd.get_dummies(pd.cut(values, bins)))
