import numpy as np

# a. Create a 2D array with random values from 0 to 1
print("(a)")
print()

ARR1 = np.random.rand(3, 4)

print(ARR1)
print()

mean_arr = np.mean(ARR1, axis=1)
std_dev_arr = np.std(ARR1, axis=1)
variance_arr = np.var(ARR1, axis=1)

print("Mean : ",mean_arr)
print("Standard Deviation : ",std_dev_arr)
print("Variance : ",variance_arr)

print()

# b. Create a 2D array of size m x n and reshape it
print("(b)")
print()

m = int(input("Enter the number of rows (m): "))
n = int(input("Enter the number of columns (n): "))

ARR2 = np.random.randint(1, 100, size=(m, n))

print()
print("Random Array : \n",ARR2)
print()

print("Shape:", ARR2.shape)
print("Type:", type(ARR2))
print("Data Type:", ARR2.dtype)
print()

ARR2_reshaped = ARR2.reshape((n, m))

print("Reshaped Array : \n",ARR2_reshaped)

print()

# c. Test elements of an array
print("(c)")
print()

ID_array = np.array([0, 1, 2, 3, np.nan, 5])

is_zero = ID_array == 0
is_non_zero = ID_array != 0
is_nan = np.isnan(ID_array)

zero_indices = np.where(is_zero)[0]
non_zero_indices = np.where(is_non_zero)[0]
nan_indices = np.where(is_nan)[0]

print("Zero Indices : ",zero_indices)
print("Non-Zero Indices : ",non_zero_indices)
print("NAN Indices : ",nan_indices)

print()

# d. Create and perform operations on arrays
print("(d)")
print()

Array1 = np.random.rand(3, 3)
Array2 = np.random.rand(3, 3)
Array3 = np.random.rand(3, 3)

Array4 = Array3 - Array2
Array5 = 2 * Array1

covariance = np.cov(Array1.flatten(), Array4.flatten())[0, 1]
correlation = np.corrcoef(Array1.flatten(), Array5.flatten())[0, 1]

print("Covariance : ",covariance)
print("Correlation : ",correlation)

print()

# e. Sum and product of two arrays
print("(e)")
print()

Array6 = np.random.rand(10)
Array7 = np.random.rand(10)

sum_first_half = np.sum(Array6[:5]) + np.sum(Array7[:5])
product_second_half = np.prod(Array6[5:]) * np.prod(Array7[5:])

print("Sum of First Half of Both Arrays : ",sum_first_half)
print("Product of Second Half of Both Arrays : ",product_second_half)

print()

# f. Size of memory occupied by an array
print("(f)")
print()

Array8 = np.random.rand(100, 100)
memory_size = Array8.nbytes

print("Random Array : ",Array8)
print()

print("Memory Size : ",memory_size)

print()

# g. Create, manipulate, and store a 2D array
print("(g)")
print()

m = 4
n = 3
Array9 = np.random.randint(10, 100, size=(m, n))

Array9[[0, 1]] = Array9[[1, 0]]
Array9[:, 1] = np.flip(Array9[:, 1])

Array10 = Array9.copy()

print("Random Array : ",Array9)

print("Array with Rows Swapped and Column Reversed : ",Array10)