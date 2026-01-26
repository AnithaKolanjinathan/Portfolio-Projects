#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


file = pd.read_csv(r'C:/Users/anith/Downloads/customer_shopping_behavior.csv')


# In[4]:


file.head(3)


# In[5]:


file.info()


# In[8]:


file.describe(include = 'all')


# In[7]:


file.isnull().sum()


# In[9]:


file['Review Rating'] = file.groupby('Category')['Review Rating'].transform(lambda x : x.fillna(x.median()))


# In[10]:


file.isnull().sum()


# In[11]:


file.columns = file.columns.str.lower()
file.columns = file.columns.str.replace(' ', '_')
file.columns


# In[12]:


file = file.rename(columns={'purchase_amount_(usd)' : 'purchase_amount'})
file.columns


# In[13]:


labels = ['Young Adult', 'Adult', 'Middle aged', 'Senior']
file['age_group'] = pd.qcut(file['age'], q=4, labels = labels)


# In[17]:


file[['age','age_group']].head()


# In[19]:


frequency_mapping = {
    'Fortnightly' : 14,
    'Weekly' : 7,
    'Monthly' : 30,
    'Quarterly' : 90,
    'Bi-Weekly' : 14,
    'Annually' : 365,
    'Every 3 Months' : 90
}

file['purchase_frequency_days'] = file['frequency_of_purchases'].map(frequency_mapping)
file[['purchase_frequency_days', 'frequency_of_purchases']].head(10)


# In[20]:


(file['discount_applied'] == file['promo_code_used']).all()


# In[21]:


file = file.drop('promo_code_used', axis = 1)


# In[22]:


file.columns


# In[23]:


pip install psycopg2-binary sqlalchemy


# In[28]:


from sqlalchemy import create_engine


# In[35]:


import urllib.parse

user = 'postgres'
password = urllib.parse.quote_plus("fgh369@A") 
host = 'localhost'
port = '5432'
db = 'customer_behaviour'

engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}')


# In[36]:


table_name = "customer"
file.to_sql(table_name, engine, if_exists = "replace", index = False)

print(f"Data successfully loaded into table '{table_name}' in database")


# In[ ]:




