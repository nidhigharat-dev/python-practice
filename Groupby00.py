#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from numpy.random import randn


# In[28]:


data = {'Company':['GOOG','AUDI','MSFT','MSFT','FB','FB'],
       'Person':['Nidhi','Virajas','Prajakta','Pradnya','Nanamika','Shakib'],
       'Sales':[200,1200,340,124,243,350]}


# In[29]:


data


# In[30]:


df = pd.DataFrame(data)


# In[31]:


df


# In[32]:


df.groupby('Company') #points to where it is stored in the memory


# In[33]:


byComp = df.groupby('Company')
byComp.mean()


# In[ ]:


df.groupby('Company').sum().loc['FB']


# In[ ]:


df


# In[ ]:


df.groupby('Company').sum().loc['GOOG']


# In[34]:


df.groupby('Company').max()


# In[35]:


df.groupby('Company').min()


# In[36]:


df.groupby('Company').describe()


# In[38]:


df.groupby('Company').describe().transpose()


# In[42]:


df.groupby('Company').describe().transpose()['AUDI']


# In[ ]:




