#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[9]:


df1 = pd.read_csv('df1',index_col=0)


# In[10]:


df1.head()


# In[11]:


df2 = pd.read_csv('df2')
df2.head()


# In[12]:


df1['A'].hist()


# In[ ]:





# In[15]:


df1['A'].plot.hist()


# In[16]:


df2.head()


# In[18]:


df2.plot.area(alpha=0.4)


# In[20]:


df2.plot.bar(stacked=True)


# In[22]:


df1['A'].hist(bins=50)


# In[24]:


df1.head()


# In[26]:


df1.plot.line(x=df1.index,y='B')


# In[30]:


df1.plot.scatter(x='A',y='B',c='C',s=df1['C']*100)


# In[31]:


df2.plot.box()


# In[33]:


df = pd.DataFrame(np.random.randn(1000,2),columns=['a','b'])
df.plot.hexbin(x='a',y='b',gridsize=25,cmap='coolwarm')


# In[35]:


df2.plot.kde()


# In[ ]:




