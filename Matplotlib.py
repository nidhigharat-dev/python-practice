#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt


# In[5]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[8]:


import numpy as np
x = np.linspace(0,5,11)
x


# In[9]:


y = x**2
y


# In[16]:


#FUNCTIONAL
plt.plot(x,y)
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')


# In[19]:


plt.subplot(1,2,1)
plt.plot(x,y,'r')

plt.subplot(1,2,2)
plt.plot(y,x,'b')


# In[23]:


#Object Orientated
fig = plt.figure() #blank canvas

#add axes
axes = fig.add_axes([0.1,0.1,0.8,0.8])

axes.plot(x,y)
axes.set_xlabel('X label')
axes.set_ylabel('Y label')
axes.set_title('Set Title')


# In[39]:


fig = plt.figure()
axes1=fig.add_axes([0.1,0.1,0.8,0.8])
axes2=fig.add_axes([0.2,0.5,0.4,0.3])

axes1.plot(x,y)
axes1.set_title('LARGER PLOT')
axes2.plot(y,x)

axes2.set_title('SMALLER PLOT')


# In[ ]:




