#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
from numpy.random import randn


# In[3]:


np.random.seed(101)


# In[4]:


df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])


# In[5]:


df


# In[6]:


#Condtional Selection


# In[7]:


df > 0


# In[12]:


booldf = df > 0
df[booldf]
#Conditional Selection along with a dataframe


# In[15]:


df['W']


# In[14]:


df['W']>0


# In[19]:


df[df['W']>0] # Removes the rows of 'W' where result is false


# In[20]:


df


# In[21]:


df[df['Z']<0]   #only occuring in row C; we are asking for entire dataframe so entire row will be retured


# In[22]:


df


# In[23]:


resultdf = df[df['W']>0]
resultdf


# In[24]:


resultdf['X']


# In[26]:


#combining the above two steps into one
df[df['W']>0]['X']
#same result


# In[29]:


# for multiple columns
df[df['W']>0][['Y','X']]


# In[32]:


boolser = df['W']>0
result = df[boolser]
result


# In[37]:


boolser2 = df['W']>0
result2 = df[boolser2]
result2


# In[38]:


mycols = ['Y','X']    
result2[mycols]


# In[40]:


df[(df['W']>0) and (df['Y']>1)]
# df does not accept "and" they require "&" operator    
# To pass on multiple conditions in paranthesis


# In[41]:


df[(df['W']>0) & (df['Y']>1)]


# In[44]:


# OR operator, using "or" will give an error
df[(df['W']>0) | (df['Y']>1)]




# In[45]:


df


# In[46]:


#Reset an Index
df.reset_index()


# In[48]:


#Does not temporarily change the index, for permanent changes use implace
#df.reset_index(inplace=True)


# In[49]:


df


# In[56]:


newind = 'CA NY WY OR CO'.split()


# In[57]:


newind


# In[58]:


df['States'] = newind


# In[59]:


df


# In[60]:


df.set_index('States')


# In[ ]:




