import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
import seaborn as sns
import warnings

from matplotlib import pyplot as plt

warnings.filterwarnings("ignore", "is_categorical_dtype")
warnings.filterwarnings("ignore", "use_inf_as_na")

#------------------------------ 1- Extraction of Data using Pandas--------------------------------------------------------

df = pd.read_csv(r'C:\Users\pc\Python_Diwali_Sales_Analysis-main\Diwali Sales Data.csv',
                 encoding='unicode_escape')  # encoding is imp

print(df.shape)                              # shape to know the df shape

print(df.head(10))                           # it will show only head 10 values


#-------------------------------2 - Cleaning / Transforming data using Pandas---------------------------------------------------

print(df.info())
# Info() used to check the columns datatype or null values
# In data last 2 columns having null values so will do cleaning
# status and unnamed were not used so to delete that will drop column

# drop unrelated/blank columns
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)
# diff column name enclosed in one single list
# axis == This parameter specifies whether to remove rows or columns. By default,
# 0=rows are removed
# 1=columns are removed
# inplace = It determines whether to modify the original DataFrame. By default, it is set to False.

print(df.info())

# to check null values .isnull() used, and it gives true /false
# print(pd.isnull(df))

# isnull() only gives the true /false value to count that values will use sum
print(pd.isnull(df).sum())  # Here we got that Amount is having 12 null values

print(df.shape)  # (11251, 13)

# to delete null values .dropna() used
df.dropna(inplace=True)  # because of inplace = true main df will change

print(df.shape)  # (11239, 13)

# Amount column is in float it needs to change to int
# .astype('int') used
df['Amount'] = df['Amount'].astype('int')

# To check column datatype .dtypes used
print(df['Amount'].dtypes)

# To check the column of df======.columns
print(df.columns)

# To rename the column name
# df.rename(columns={'Marital_Status':'Shadi'})  #inplace did not use, so it will not save

# describe()-It returns description of dta in the Dataframe(i.e count,mean,std etc)
print(df.describe())

# To describe specific column
print(df[['Age', 'Orders', 'Amount']].describe())

# ===============Exploratory Data Analysis using Seaborn and matplotlib ==================================================================

# Gender
# print(df.columns())

# creating Countplot --It will count no of records by category(Gender)
ax = sns.countplot(x='Gender', data=df)

#To give labels to graph
for bars in ax.containers:
    ax.bar_label(bars)     # Due to this number will visible
plot.show()                # It used to show graph
