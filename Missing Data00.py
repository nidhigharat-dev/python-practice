#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from numpy.random import randn


# In[3]:


d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}
df = pd.DataFrame(d)
df


# In[7]:


df.dropna(axis = 0) #pandas drops any row with missing values


# In[6]:


df.dropna(axis = 1) #performed for columns


# In[8]:


df


# In[10]:


df.dropna(thresh=2) # keep row with atleast 2 non-NA values


# In[11]:


df


# In[12]:


df.fillna(value='FILL VALUE')


# In[14]:


#filling the value with the mean of the column
df['A'].fillna(value=df['A'].mean())


# In[ ]:




