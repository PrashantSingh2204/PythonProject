import pandas as pd
names=["Prashant","saurabh"]
nameList=pd.Series(names)

#print(nameList)

# # Load , the data , 
# # Convert it to series ,
# # Find the total values , size , etc basic know how of the day
# # Do some stats - min , mid , max ,meagan , var , std etc

#SalesData=pd.read_excel("E:\PythonProject\PandaProject\Data\sales_revenue.xlsx")
#print(SalesData)
# revenueData=SalesData["Sales Revenue"]
# print("Revenue Data :",revenueData)
# print("Revenue Data Total:",revenueData.sum())
# print("Revenue Data -Size:",revenueData.size)
# print("Revenue Data -MIN:",revenueData.min())
# print("Revenue Data -Mid:",revenueData.median())
# print("Revenue Data -Max:",revenueData.max())
# print("Revenue Data -meagan:",revenueData.mean())
# print("Revenue Data -Var:",revenueData.var())
# print("Revenue Data -std:",revenueData.std())


#############################################################################

iphoneSalesData=pd.read_excel("E:\PythonProject\PandaProject\Data\iphone_sales_data.xlsx")
#print(iphoneSalesData)
condition=(iphoneSalesData["Sales_Channel"] =="Online") & (iphoneSalesData["Sales_Region"] == "Asia Pacific")
print(iphoneSalesData[condition]["Quantity_Sold"].sum())
