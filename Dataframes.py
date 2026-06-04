#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[3]:


from numpy.random import randn


# In[4]:


np.random.seed(101)


# In[6]:


df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])


# In[8]:


df


# In[9]:


df['W']


# In[15]:


type(df['W'])


# In[ ]:


#Series received


# In[11]:


df.W


# In[13]:


df[['W','Z']]


# In[16]:


#dataframe received


# In[19]:


df['new'] = df['W'] + df['Y']
df


# In[21]:


df.drop('new',axis = 1)


# In[22]:


df


# In[23]:


df.drop('new',axis = 1, inplace = True)


# In[24]:


df #column permanently removed


# In[26]:


df.drop('E',axis=0)


# In[28]:


df


# In[29]:


df.shape


# In[31]:


df[['Z','X']]


# In[32]:


df


# In[33]:


df.loc['A']


# In[34]:


#series


# In[35]:


df.iloc[2] #index location


# In[36]:


df.loc['B','Y']


# In[37]:


df


# In[38]:


df.loc[['A','B'],['W','Y']] #RETURNING SUBSET


# In[ ]:




