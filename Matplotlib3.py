#!/usr/bin/env python
# coding: utf-8

# In[37]:


import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,5,11)
x
y = x**2
y
fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

ax.plot(x,y,color='#FF8C00', lw=1,alpha=0.5,ls=':',marker='o',ms=10,mfc='purple',mew=7,mec='pink') #RGB HEX CODE


# In[20]:


x


# In[ ]:




