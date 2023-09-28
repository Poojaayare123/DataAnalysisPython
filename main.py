import pandas as pd
import csv
import os
df =pd.read_csv(r'C:\Users\pc\Python_Diwali_Sales_Analysis-main\Diwali Sales Data.csv', encoding='unicode_escape')  #encoding is imp

print(df.shape)  #shape to know thedf shape

print(df.head(10))  #it will show only head 10 values

#here last 2 columns having null values so willdo cleaning

