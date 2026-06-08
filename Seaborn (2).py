#!/usr/bin/env python
# coding: utf-8

# In[69]:


import seaborn as sns


# In[70]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[71]:


tips = sns.load_dataset('tips') #Seaborn built-in-dataset


# In[72]:


tips.head()


# In[73]:


#distribution plot (univariate) Histogram
sns.displot(tips['total_bill'],kde=False,bins=40)
#KDE kerner distribution


# In[74]:


sns.jointplot(x='total_bill',y='tip',data=tips) #Bivariate


# In[75]:


sns.pairplot(tips,hue='sex',palette='coolwarm') #generates for all the columns in the dataset


# In[76]:


sns.rugplot(tips['total_bill'])


# In[77]:


sns.kdeplot(tips['total_bill'])


# In[78]:


import numpy as np 


# In[79]:


sns.barplot(x='sex',y='total_bill',data=tips,estimator=np.std,color='red')


# In[80]:


sns.countplot(x='sex',data=tips)


# In[81]:


sns.boxplot(x='day',y='total_bill',data=tips,hue='smoker')


# In[82]:


sns.violinplot(x='day',y='total_bill',data=tips,hue='sex',split=True)


# In[83]:


sns.stripplot(x='day',y='total_bill',data=tips,jitter=True,hue='sex')


# In[84]:


sns.violinplot(x='day',y='total_bill',data=tips,color='pink')
sns.swarmplot(x='day',y='total_bill',data=tips,hue='sex')
#sometimes they dont scale to very large datasets


# In[88]:


flights = sns.load_dataset('flights')
flights.head()


# In[89]:


tips.head()


# In[90]:


tc = tips.corr()
sns.heatmap(tc, annot=True,cmap='coolwarm')


# In[95]:


fp = flights.pivot_table(index='month',columns='year',values='passengers')
fp


# In[101]:


sns.heatmap(fp,cmap='magma',linecolor='white',linewidths=1)


# In[102]:


sns.clustermap(fp)


# In[9]:


import seaborn as sns
import matplotlib.pylab as plt
get_ipython().run_line_magic('matplotlib', 'inline')
iris = sns.load_dataset('iris')
iris.head()


# In[ ]:





# In[10]:


iris['species'].unique()


# In[14]:


g = sns.PairGrid(iris)
g.map_diag(sns.distplot)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)


# In[15]:


tips = sns.load_dataset('tips')


# In[16]:


tips.head()


# In[23]:


g = sns.FacetGrid(data=tips,col='time',row='smoker')
g.map(plt.scatter,'total_bill','tip')


# In[24]:


import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
tips = sns.load_dataset('tips')
tips.head()


# In[34]:


sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',markers=['o','v'],scatter_kws={'s':100})



# In[42]:


sns.lmplot(x='total_bill',y='tip',data=tips,col='day',hue='sex',
           aspect=0.6)


# In[54]:


sns.set_context('poster')
sns.countplot(x='sex',data=tips)


# In[ ]:




