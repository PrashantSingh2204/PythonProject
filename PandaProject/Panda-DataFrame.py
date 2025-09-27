import pandas as pd

print("**************************************************")
customerCSVData=pd.read_csv("E:\PythonProject\PandaProject\customers-100.csv")
print(type(customerCSVData["Index"]))

print(type(customerCSVData))
print(customerCSVData)
print(customerCSVData.describe)
print("Info",customerCSVData.info)