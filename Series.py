#!/usr/bin/env python
# coding: utf-8

# #### **Series- similar to numpy array, can be indexed by label**

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


labels = ['a','b','c']


# In[3]:


my_data = [10,20,30]


# In[4]:


arr = np.array(my_data)
d = {'a':10, 'b':20, 'c':30}


# In[5]:


labels


# In[6]:


my_data


# In[7]:


arr


# In[8]:


d


# In[9]:


pd.Series(data = my_data)


# In[10]:


pd.Series(data=my_data, index=labels)


# In[11]:


pd.Series(my_data,labels)


# In[13]:


pd.Series(arr,labels)


# In[14]:


pd.Series(d)


# In[16]:


#flexibility of panda series- not possible with numpy array
pd.Series(data=[sum,print,len])


# In[17]:


ser1 = pd.Series([1,2,3,4],['USA','Germany','USSR','Japan'])


# In[18]:


ser1


# In[19]:


ser2 = pd.Series([1,2,5,4],['USA','Germany','Italy','Japan'])


# In[20]:


ser2


# In[21]:


ser1['USA']


# In[22]:


ser3 = pd.Series(data=labels)
ser3


# In[23]:


ser1 + ser2


# In[24]:


#integers converted into floats


# In[ ]:




