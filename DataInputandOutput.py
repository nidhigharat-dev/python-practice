#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from numpy.random import randn


# In[2]:


pwd


# In[3]:


pd.read_csv('example')


# In[4]:


df = pd.read_csv('example')


# In[5]:


df


# In[8]:


df.to_csv('My_output',index=False)


# In[9]:


pd.read_csv('My_output')


# In[13]:


pd.read_excel('Excel_Sample.xlsx',sheet_name='Sheet1')


# In[14]:


df.to_excel('Excel_Sample2.xlsx',sheet_name='NewSheet')


# In[15]:


data = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html')


# In[17]:


type(data) #not a dataframe


# In[19]:


data[0].head()


# In[22]:


from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:')


# In[24]:


df.to_sql('my_table',engine)


# In[ ]:




