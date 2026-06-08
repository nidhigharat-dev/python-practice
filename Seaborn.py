#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


tips = sns.load_dataset('tips') #Seaborn built-in-dataset


# In[4]:


tips.head()


# In[16]:


#distribution plot (univariate) Histogram
sns.displot(tips['total_bill'],kde=False,bins=40)
#KDE kerner distribution


# In[21]:


sns.jointplot(x='total_bill',y='tip',data=tips) #Bivariate


# In[24]:


sns.pairplot(tips,hue='sex',palette='coolwarm') #generates for all the columns in the dataset


# In[25]:


sns.rugplot(tips['total_bill'])


# In[ ]:


#KDE- kernel distribution estimation

