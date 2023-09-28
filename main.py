import pandas as pd
import csv
import os

df = pd.read_csv(r'C:\Users\pc\Python_Diwali_Sales_Analysis-main\Diwali Sales Data.csv',
                 encoding='unicode_escape')  # encoding is imp

print(df.shape)  # shape to know the df shape

print(df.head(10))  # it will show only head 10 values

# here last 2 columns having null values so will do cleaning

print(df.info())
# info used to check the columns datatype or null values
# here status and unnamed were not used so to delete that will  drop column

# drop unrelated/blank col
df.drop(['Status', 'unnamed1'],axis=1, inplace=True)  #diff column name enlosed in one single list
# axis ==is to delete whole column ---This parameter specifies whether to remove rows or columns. By default,
# it is set to 0, which means rows are removed. If you want to remove columns, set it to 1. #inplace = This parameter
# is a boolean value that determines whether to modify the original DataFrame in place. By default, it is set to False.

print(df.info())

#to check null values =====.isnull() --it gives true /false

