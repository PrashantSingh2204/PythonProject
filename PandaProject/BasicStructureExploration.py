import pandas as pd

# 1.  Print the total number of rows and columns present in the 
# dataset using attributes.
supermarket_data = pd.read_csv('PandaProject/Data/supermart_retail.csv')
print("Total number of rows and columns:", supermarket_data.shape)
  

# 2.  Display the names of all columns and the data types of each column.
print("Column names and data types:")
print(supermarket_data.dtypes)

# 3.  Show the first ten rows and the last five rows of the DataFrame.
print("First ten rows:")
print(supermarket_data.head(10))
print("Last five rows:")
print(supermarket_data.tail())

# 4.  Display the index and column labels separately.
print("Index labels:")
print(supermarket_data.index)
print("Column labels:")
print(supermarket_data.columns)

# 5.  Print the shape of the DataFrame and explain what each number means.
print("Shape of the DataFrame:", supermarket_data.shape)
print("Number of rows:", supermarket_data.shape[0])
print("Number of columns:", supermarket_data.shape[1])

# 6.  Use the describe() method to get summary statistics of all numerical columns.
print("Summary statistics of numerical columns:")
print(supermarket_data.describe())

# 7.  Use the info() method to display column names, non-null counts, and data types.
print("DataFrame info:")
print(supermarket_data.info())

# 8.  Find the minimum, maximum, mean, and standard deviation of the sales column.
print("Sales column statistics:")
print("Minimum sales:", supermarket_data['Sales'].min())
print("Maximum sales:", supermarket_data['Sales'].max())
print("Mean sales:", supermarket_data['Sales'].mean())
print("Standard deviation of sales:", supermarket_data['Sales'].std())

# 9.  Use the median(), sum(), and count() methods to calculate values for the profit column.
print("Profit column statistics:")
print("Median profit:", supermarket_data['Profit'].median())
print("Total profit:", supermarket_data['Profit'].sum())
print("Count of profit entries:", supermarket_data['Profit'].count())

# 10. Use quantile() to find the 25th, 50th, and 75th percentiles of the discount column.
print("Discount column percentiles:")
print("25th percentile:", supermarket_data['Discount'].quantile(0.25))
print("50th percentile:", supermarket_data['Discount'].quantile(0.50))
print("75th percentile:", supermarket_data['Discount'].quantile(0.75))

