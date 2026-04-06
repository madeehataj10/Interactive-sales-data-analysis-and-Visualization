import pandas as pd
import matplotlib.pyplot as plt#%matplotlib inline
import seaborn as sns
dataset = "E:\\My Works\\My Career\\Projects\\Data Analysis & Machine Learning\\Expolatory Data Analysis\\Sales Data Analysis\\Sales Analysis\\Dataset\\superstore_sales.xlsx"
sales = pd.read_excel(dataset)
sales.head()
sales.tail()
sales.shape
sales.columns
sales.dtypes
sales.isnull().sum()
sales.describe()
sales.duplicated().sum()
for columns in sales.columns:
  print(columns)
sales.info()
sales.isnull().sum()
sales.describe()
sales.info()
sales['month_year'] = sales['order_date'].apply(lambda x: x.strftime('%Y-%m'))
sales['month_year'].sample(10)
sales.head()
sales_by_month = sales.groupby('month_year').sum()['sales'].reset_index()
plt.figure(figsize=(15,6))
plt.plot(sales_by_month['month_year'], sales_by_month['sales'])
plt.xticks(rotation='vertical', size=8)
plt.show()
plt.figure(figsize=(15,6))
plt.bar(sales_by_month['month_year'], sales_by_month['sales'])
plt.xticks(rotation='vertical', size=8)
plt.show()
products_sales = pd.DataFrame(sales.groupby('product_name').sum()['sales'])
products_sales = products_sales.sort_values('sales', ascending=False)
products_sales[:10]
products_by_quantity = pd.DataFrame(sales.groupby('product_name').sum()['quantity'])
products_by_quantity_sorted = products_by_quantity.sort_values('quantity', ascending=False)
products_by_quantity_sorted[:10]
plt.figure(figsize=(10,8.5))
sns.countplot(sales['ship_mode'])
plt.show()
ship_mode = pd.DataFrame(sales['ship_mode'].value_counts()).reset_index()
ship_mode = ship_mode.rename({'index': 'shipping_mode', 'ship_mode': 'count'}, axis=1)
ship_mode.head()
fig = plt.figure(figsize =(10, 7))
plt.pie(ship_mode['count'], labels = ship_mode['shipping_mode'])
plt.show()
cateory_by_profit = pd.DataFrame(sales.groupby(['category','sub_category']).sum()['profit'])
cateory_by_profit.sort_values(['profit'], ascending=False)
sales['customer_name'].value_counts().head(10)
plt.figure(figsize=(10,8.5))
sns.countplot(sales['segment'])
plt.show()
by_segment = pd.DataFrame(sales.groupby('segment').sum()['quantity'])
by_segment_sort = by_segment.sort_values('quantity', ascending=False)
by_segment_sort
by_segment_p = pd.DataFrame(sales.groupby('segment').sum()['profit'])
by_segment_sort_p = by_segment_p.sort_values('profit', ascending=False)
by_segment_sort_p
sales['country'].value_counts().head(15)
plt.figure(figsize=(16,9))
sns.countplot(sales['region'])
plt.show()
by_shiping_cost = pd.DataFrame(sales.groupby('sub_category').sum()['shipping_cost'])
by_shiping_cost_sort = by_shiping_cost.sort_values('shipping_cost', ascending=False)
by_shiping_cost_sort
sales['shiping_days'] = sales['ship_date'] - sales['order_date']
sales.head(5)
sales['shiping_days'].value_counts()
sales['market'].value_counts()
plt.figure(figsize=(16,9))
sns.countplot(sales['market'])
plt.show()
