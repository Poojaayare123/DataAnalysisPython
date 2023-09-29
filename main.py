import pandas as pd
import numpy as np
import matplotlib.pyplot as plot
import seaborn as sns
import warnings

from matplotlib import pyplot as plt

warnings.filterwarnings("ignore", "is_categorical_dtype")
warnings.filterwarnings("ignore", "use_inf_as_na")

# ------------------------------ 1- Extraction of Data using Pandas--------------------------------------------------------

df = pd.read_csv(r'C:\Users\pc\Python_Diwali_Sales_Analysis-main\Diwali Sales Data.csv',
                 encoding='unicode_escape')  # encoding is imp

print(df.shape)                              # shape to know the df shape

print(df.head(10))                           # it will show only head 10 values


# -------------------------------2 - Cleaning / Transforming data using Pandas---------------------------------------------------

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
# ax = sns.countplot(x='Gender', data=df)
#
# #To give labels to graph
# for bars in ax.containers:
#     ax.bar_label(bars)     # Due to this number will visible
# # plot.show()                # It used to show graph


#
# sales_gen=df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
# this will give groping of gender based on feamle and male and will give total amount(shopping) spend by female and male
# we did groupby based on gender basis an include sum of amount and sort that on amount
# print(sales_gen)
#
# sns.barplot(x='Gender',y='Amount', data=sales_gen)
# plot.show()

# Conclusion 1:From graph we get to know that most of the buyers are female

# #--------------------------Based on Age-group------------------------------
#
# ax=sns.countplot(data=df, x='Age Group', hue='Gender')  # to show this properly commented above gender code
#
# # plot.show()
# for bars in ax.containers:
#     ax.bar_label(bars)
# # plot.show()
#
#
# #Total Amount vs Total age
# sales_age=df.groupby(['Age Group'] ,as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
#
# sns.barplot(x='Age Group',y='Amount',data=sales_age)
# plot.show()
#
# #conclusion 2-- From above graph most of the buyers are of age gropu between 16-35yrs female


# ----------------------based on state--------------------------------------------------------------
# # ----------------------------------find total number of orders from the top 10 states----------------------------
# sales_state=df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
# # as_index--determines whether the columns you group by should become the index of the resulting DataFrame.
# # False in order to preserve the original structure of your data.
#
# # To give the size of graph
# sns.set(rc={'figure.figsize':(15,5)})  #widhth,height
#
# # create plot using state and orders
# sns.barplot(data=sales_state,x='State',y='Orders')
# plot.show()
#
# # # Above graph shows that most of the ordersare from UP,maharashatra and karnatka and alsoshows top 10 states
#
# # -----------------------------find total amount/sales from top 10 states-----------------------------------------
# sales_amount=df.groupby(['State'],as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
#
# # To give the size of graph
# sns.set(rc={'figure.figsize':(15,5)})  #widhth,height
#
# sns.barplot(x='State', y='Amount', data=sales_amount)
# plot.show()
#
# # conclusion 3-- We can see that most of the orders nd sales /amount from UtterPradesh ,Maharashtra and karnataka

# # -------------------------------Based on marital status----------------------------------------------------------
# # Find out who are the most buyers
#
# # 1st will create counterplot for marital status
# ax=sns.countplot(data=df,x='Marital_Status')
# sns.set(rc={'figure.figsize':(5,5)})
# for bars in ax.containers:
#     ax.bar_label(bars)
# plot.show()
#
# #Based on marital status and gender find out who spend more amount on shopping
# sales_buyers= df.groupby(['Marital_Status','Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
#
# sns.barplot(data=sales_buyers,x='Marital_Status',y='Amount',hue='Gender')
# plot.show()

# on graph 1e7 means 10 raised to power 7
# conclusion 4-Most of the buyers are married women and they have high purchasing power
#
# # ----------------------------Based on Occupation----------------------
# # Find out most of the  buyers are from which industry
# ax=sns.countplot(data=df, x='Occupation')  #beacause of countplot gotto know count of every industry
# sns.set(rc={'figure.figsize':(20,5)})
# for bars in ax.containers:
#     ax.bar_label(bars)
# # plot.show()
#
# sales_occupation=df.groupby(['Occupation'], as_index=False) ['Amount'].sum().sort_values(by='Amount',ascending=False)
# sns.barplot(data=sales_occupation,x='Occupation',y='Amount')
# plot.show()
#
# # conclusion 5-Most of the buyers are working in IT ,healthcare and aviation
#
# #----------------------------Based on Product Category------------------------------------
# # print(df.columns)
# ax=sns.countplot(data=df, x='Product_Category')
# sns.set(rc={'figure.figsize':(40,5)})
# for bars in ax.containers:
#     ax.bar_label(bars)
# # plot.show()
#
# sales_Product=df.groupby(['Product_Category'], as_index=False) ['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)
# sns.set(rc={'figure.figsize':(40,5)})
# sns.barplot(data=sales_Product,x='Product_Category', y='Amount')
# plot.show()
#
# # conclusion 6-Most of the sold products are from food, clothing and electronics category

#----------------------------Top 10 most sold products based onorders--------------------------------------------

sales_Product=df.groupby(['Product_ID'], as_index=False) ['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)
sns.set(rc={'figure.figsize':(40,5)})
sns.barplot(data=sales_Product,x='Product_ID', y='Orders')
plot.show()

#conclusion 7-- It gives TOp 10 ProductID

# -------------------------------------------Final Conclusion-----------------------------------------
# Married women age group 26-35yrsfrom UP, Maharashtra and Karnataka working in IT ,Healthcare and aviation are more likely to buy products from food
# , clothing and electronics category