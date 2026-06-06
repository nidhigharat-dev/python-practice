#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from numpy.random import randn


# In[4]:


df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})
df.head()


# In[5]:


df['col2'].unique()


# In[11]:


df['col2'].nunique()


# In[12]:


df['col2'].value_counts()


# In[13]:


df[df['col1']>2]


# In[14]:


df['col2']>2


# In[16]:


df[(df['col1']>2) & (df['col2']==444)]


# In[17]:


def times2(x):
    return x*2


# In[18]:


df['col1'].sum()


# In[19]:


df['col1'].apply(times2)


# In[20]:


df['col3']


# In[21]:


df['col3'].apply(len)


# In[23]:


df['col2'].apply(lambda x: x*2)


# In[24]:


df


# In[26]:


df.drop('col1',axis=1)
#df.drop('col1',axis=1,inplace=True)


# In[27]:


df


# In[31]:


df.columns


# In[32]:


df.index


# In[33]:


df


# In[36]:


df.sort_values(by='col2')


# In[37]:


df.isnull()


# In[38]:


data = {'A':['foo','foo','foo','bar','bar','bar'],
     'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}

df = pd.DataFrame(data)


# In[39]:


df


# In[40]:


df.pivot_table(values='D',index=['A','B'],columns=['C'])


# In[ ]:




