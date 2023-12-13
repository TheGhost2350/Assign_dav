import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
data = pd.DataFrame(data=iris.data, columns=iris.feature_names)
data['target'] = iris.target

print("(a) Display dataset information")
print("Dataset Information:")
print(data.info())
print()

print("(b) Find the number of missing values")
missing_values = data.isnull().sum()
print("\nNumber of Missing Values in Each Column:")
print(missing_values)
print()

print("(c) Plot bar chart for class label frequency")
plt.figure(figsize=(6, 4))
sns.countplot(data['target'])
plt.xlabel('Iris Flower Type')
plt.ylabel('Frequency')
plt.title('Frequency of Each Iris Flower Type')
plt.show()
print()

print("(d) Scatter plot for Petal Length vs Sepal Length")
plt.figure(figsize=(6, 4))
sns.scatterplot(x=data['sepal length (cm)'], y=data['petal length (cm)'], hue=data['target'])
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.title('Scatter Plot: Petal Length vs Sepal Length')
plt.show()
print()

print("(e) Plot density distribution for Petal width")
plt.figure(figsize=(6, 4))
sns.kdeplot(data['petal width (cm)'], fill=True)
plt.xlabel('Petal Width (cm)')
plt.ylabel('Density')
plt.title('Density Distribution of Petal Width')
plt.show()
print()

print("(f) Use a pair plot for pairwise bivariate distribution")
sns.pairplot(data, hue='target')
plt.show()
print()

print("(g) Draw a heatmap for two numeric attributes")
numeric_attributes = data.select_dtypes(include=['float64'])
sns.heatmap(numeric_attributes.corr(), annot=True)
plt.show()
print()

print("(h) Compute basic statistics for numeric features")
statistics = data.describe()
print("\nStatistics for Numeric Features:")
print(statistics)
print()

print("(i) Compute correlation coefficients and plot a heatmap")
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True)
plt.show()
