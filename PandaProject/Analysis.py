import pandas as pd              # Primary library for data manipulation and analysis
import numpy as np               # Numerical computing library for mathematical operations

# Data visualization libraries
# import matplotlib.pyplot as plt  # Basic plotting library
# import seaborn as sns           # Statistical data visualization library
# import plotly.express as px     # Interactive plotting library
# import plotly.graph_objects as go # Advanced plotly graphics

# Statistical analysis
# from scipy import stats         # Statistical functions and tests
# from sklearn.preprocessing import StandardScaler, MinMaxScaler  # Data preprocessing

# # System and warnings
# import warnings
# import sys
# import os
# from datetime import datetime


supermarketData=pd.read_csv("E:\Panda-demo\Panda\supermart_retail.csv")
#print(supermarketData)
#condition=(supermarketData["City"] =="Dindigul") & (supermarketData["Region"] == "South") & (supermarketData["Profit"]>500)
#print(supermarketData[condition])
#print(supermarketData[(supermarketData["City"] =="Dindigul") & (supermarketData["Region"] == "South") & (supermarketData["Profit"]>500)])

#Calculate the total profit made from the “Beverages” category.
# condition=(supermarketData["Category"] =="Beverages") 
# print("Profit",supermarketData[condition])
# print("Profit",supermarketData[condition]["Profit"].sum())



#Write a Python program using pandas to display all rows 
#Where sales is greater than one thousand and profit is greater than three hundred and region is south.

# condition=(supermarketData["Sales"] >1000) & (supermarketData["Profit"] >300) & (supermarketData["Region"] == "South")
# print(supermarketData[condition])

# 10.Show all records where region is west and category is beverages and sub category is cold drinks 
# and sales is greater than one thousand and profit is less than two hundred and discount is greater than point one five.

# 11.Display all orders 
# where category is not food grains and sales is greater than fifteen hundred and profit is more than five hundred 
# and discount is between point two and point three and city contains the word market.
result11 = supermarketData[(supermarketData["Category"] != "Food Grains") &
              (supermarketData["Sales"] > 1500) &
              (supermarketData["Profit"] > 500) &
              (supermarketData["Discount"].between(0.2, 0.3)) &
              (supermarketData["City"].str.contains("market", case=False))]

#print(result11)

# 12.Filter all rows where category is beverages and sales minus discount multiplied by sales is greater than one thousand 
# and region is south and profit is less than three hundred.


# 13.Show all records where sub category length is greater than ten characters and sales is more than one thousand 
# and discount is less than point one five and profit is greater than four hundred.


# 14.Display all orders where category is fruits and veggies and profit is more than average profit 
# and sales is more than average sales and discount is less than average discount.

averageProfit=supermarketData["Profit"].mean()
averagesales=supermarketData["Sales"].mean()
averagediscount=supermarketData["Discount"].mean()

# condition=(supermarketData["Category"]== "Fruits & Veggies") \
#             & (supermarketData["Profit"] >averageProfit) & (supermarketData["Discount"] >averagediscount)
# print(supermarketData[condition])

# 1.Show all rows
#  where sales is greater than twice the profit and profit is less than the average profit and discount is below 0.2.
condition=(supermarketData["Sales"] > (supermarketData["Profit"]*2)) \
            & (supermarketData["Profit"] >averageProfit) & (supermarketData["Discount"] < 0.2)

supermarketData["Condition"]=condition
#print( supermarketData[condition][["Customer Name","Category"]] )
print(supermarketData)

# 2.Display all records where profit is greater than half of the maximum profit and sales is less than the median sales.

# 3.Filter the data where discount is greater than the average discount and profit percentage calculated as profit divided by sales multiplied by one hundred is less than twenty.

# 4.Show all rows where sales is less than the maximum sales and profit is greater than the minimum profit and discount is between point one and point two five.

# 5.Retrieve all records where sales minus profit is greater than the average of sales minus profit and discount is below the median discount.

# 6.Display rows where profit is more than thirty percent of the maximum profit and sales is greater than the median sales but discount is less than avg Discount
