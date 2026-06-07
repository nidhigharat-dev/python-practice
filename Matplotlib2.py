#!/usr/bin/env python
# coding: utf-8

# In[6]:


import matplotlib.pyplot as plt


# In[7]:


import numpy as np
x = np.linspace(0,5,11)
y = x**2


# In[12]:


#fig,axes = plt.subplots(nrows=3,ncols=3)
#plt.tight_layout()
#axes.plot(x,y)


# In[18]:


fig,axes = plt.subplots(nrows=1,ncols=2)

axes[0].plot(x,y)
axes[0].set_title('First Plot')
axes[1].plot(y,x)
axes[1].set_title('Second Plot')

for current_ax in axes:
    current_ax.plot(x,y)

plt.tight_layout()


# In[14]:


axes


# In[43]:


fig = plt.figure(figsize=(8,2))

ax= fig.add_axes([0,0,1,1])
ax.plot(x,x**2, label ='X Squared')
ax.plot(x,x**3, label ='X Cubed')
ax.plot(x,x**4, label ='X Multiplied')
ax.legend(loc=9)


# In[24]:


fig,axes = plt.subplots(nrows=2,ncols=1,figsize=(8,2))
axes[0].plot(x,y)
axes[1].plot(y,x)
plt.tight_layout()


# In[25]:


fig


# In[26]:


fig.savefig('my_picture.png',dpi=200)


# In[ ]:




