#!/usr/bin/env python
# coding: utf-8

# ### *Multi Index*

# In[9]:


import numpy as np
import pandas as pd
from numpy.random import randn


# In[10]:


# Index Levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)


# In[11]:


outside


# In[12]:


inside


# In[13]:


hier_index


# In[15]:


df = pd.DataFrame(randn(6,2),hier_index,['A','B'])
df


# In[16]:


df.loc['G1']


# In[17]:


df.loc['G1'].loc[1]


# In[18]:


df.index.names


# In[19]:


df


# In[20]:


df.index.names = ['Groups','Num']


# In[23]:


df


# In[27]:


df.loc['G2'].loc[2].loc['B']


# In[31]:


df.loc['G1'].loc[3].loc['B']


# In[32]:


# Cross section funtion


# In[33]:


df


# In[34]:


df.loc['G1']


# In[35]:


df.xs('G1')


# In[36]:


df


# In[37]:


# Collecting elements from both the groups at once is difficult, hence we use xs for multiselection


# In[38]:


df.xs(1,level='Num')


# In[39]:


df


# In[ ]:





# In[ ]:




