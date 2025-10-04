from numpy import where
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

#What  is the average profit margins for sub category “Food Grains”  in  cities : Vellore , Krishnagiri or Perambalur
food_grains_cities = supermarket_data[(supermarket_data['Category'] == 'Food Grains') & 
                                       (supermarket_data['City'].isin(['Vellore', 'Krishnagiri', 'Perambalur']))]

average_profit_margin = food_grains_cities['Profit'].mean()
print("Average profit margin for Food Grains in selected cities:", average_profit_margin)


#Get all rows where Category is "Beverages", Region is "South", and Sales is greater than 800. using loc
beverages_south = supermarket_data.loc[(supermarket_data['Category'] == 'Beverages') & 
                                       (supermarket_data['Region'] == 'South') & 
                                       (supermarket_data['Sales'] > 800)]

print("Beverages in South with Sales > 800:")
print(beverages_south)

#Show rows where State is "Tamil Nadu", Discount is less than 0.2, and City is not "Vellore".
tamil_nadu_discounts = supermarket_data.loc[(supermarket_data['State'] == 'Tamil Nadu') & 
                                             (supermarket_data['Discount'] < 0.2) & 
                                             (supermarket_data['City'] != 'Vellore')]

print("Tamil Nadu with Discount < 0.2 and City != Vellore:")
print(tamil_nadu_discounts)

#Display orders where Category is "Food Grains", Sales is above 1500, and Profit is below 300.
food_grains_orders = supermarket_data.loc[(supermarket_data['Category'] == 'Food Grains') & 
                                           (supermarket_data['Sales'] > 1500) & 
                                           (supermarket_data['Profit'] < 300)]

print("Food Grains orders with Sales > 1500 and Profit < 300:")
print(food_grains_orders)

#Retrieve rows where Region is "North", Category is "Oil & Masala", and Order Year is 2017.
oil_masala_north = supermarket_data.loc[(supermarket_data['Region'] == 'North') & 
                                         (supermarket_data['Category'] == 'Oil & Masala') & 
                                         (supermarket_data['Order Date'].dt.year == 2017)]

print("Oil & Masala in North for 2017:")
print(oil_masala_north)

#Find rows where Discount is more than 0.1, Profit is between 100 and 400, and City contains the letter "r".
discounted_profit_cities = supermarket_data.loc[(supermarket_data['Discount'] > 0.1) & 
                                                 (supermarket_data['Profit'].between(100, 400)) & 
                                                 (supermarket_data['City'].str.contains('r', case=False))]

print("Cities with Discount > 0.1, Profit between 100 and 400, and 'r' in City:")
print(discounted_profit_cities)

#Select orders where Category is "Beverages" or "Food Grains", Region is not "West", and Sales is less than 2000.
beverages_food_grains = supermarket_data.loc[((supermarket_data['Category'] == 'Beverages') | 
                                               (supermarket_data['Category'] == 'Food Grains')) & 
                                              (supermarket_data['Region'] != 'West') & 
                                              (supermarket_data['Sales'] < 2000),["Category","Region","Sales"]]

print("Beverages or Food Grains not in West with Sales < 2000:")
print(beverages_food_grains)

#Get all rows where City is "Krishnagiri", Profit is above 200, and Discount is between 0.1 and 0.2.
krishnagiri_orders = supermarket_data.loc[(supermarket_data['City'] == 'Krishnagiri') & 
                                           (supermarket_data['Profit'] > 200) & 
                                           (supermarket_data['Discount'].between(0.1, 0.2))]

print("Krishnagiri orders with Profit > 200 and Discount between 0.1 and 0.2:")
print(krishnagiri_orders)

#Show rows where Category is not "Masalas", Sales is above 1000, and Region is either "South" or "West".
non_masalas_sales = supermarket_data.loc[(supermarket_data['Category'] != 'Masalas') & 
                                          (supermarket_data['Sales'] > 1000) & 
                                          (supermarket_data['Region'].isin(['South', 'West']))]

print("Non-Masalas with Sales > 1000 in South or West:")
print(non_masalas_sales)

#Retrieve rows where Category is "Beverages", State is "Tamil Nadu", Discount is below 0.15, and Profit is greater than 150.
beverages_tamil_nadu = supermarket_data.loc[(supermarket_data['Category'] == 'Beverages') & 
                                             (supermarket_data['State'] == 'Tamil Nadu') & 
                                             (supermarket_data['Discount'] < 0.15) & 
                                             (supermarket_data['Profit'] > 150)]

print("Beverages in Tamil Nadu with Discount < 0.15 and Profit > 150:")
print(beverages_tamil_nadu)


#Show rows where Category is not contains "Masalas", Sales is above 1000, and Region is either "South" or "West".
non_masalas_sales = supermarket_data.loc[~supermarket_data['Category'].str.contains('Masalas', case=False) & 
                                          (supermarket_data['Sales'] > 1000) & 
                                          (supermarket_data['Region'].isin(['South', 'West']))]
print("Non-Masalas with Sales > 1000 in South or West:")
print(non_masalas_sales)
