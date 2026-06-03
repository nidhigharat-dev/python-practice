#!/usr/bin/env python
# coding: utf-8

# ### **NumPy**
# #### **Linear Algebra Library**
# ##### *Numpy Arrays- Vectors 1D or Matrices 2D*

# ##### *Casting list as a numpy array*

# In[2]:


my_list = [1,2,3]
my_list


# In[4]:


import numpy as np
arr = np.array(my_list)
arr


# In[6]:


my_mat = [[2,3,4],[3,4,6],[4,3,6]]
my_mat


# In[7]:


np.array(my_mat)


# In[10]:


np.arange(0,11,2)


# In[11]:


np.zeros(3)


# In[14]:


np.zeros((4,3))


# In[15]:


np.ones(4)


# In[16]:


np.ones((2,5))


# ### 1D array [
# ### 2D array [[
# ### 3D array [[[

# ###### *ARRANGE WILL TAKE THIRD ARGUMENT AS THE STEP SIZE YOU WANT*
# ###### *lINSPACE WILL TAKE THE THIRD ARGUMENT AS THE NUMBER OF POINTS YOU WANT*

# In[20]:


np.linspace(3,4,2)
# START, STOP, NO OF POINTS


# In[24]:


np.linspace(3,4,80)
# Result has one [ so it is a 1D vector


# In[25]:


# Identity Matrix using numpy
np.eye(4)


# In[28]:


# Creating a random array between 0 and 1
#random.TAB

np.random.rand(4)


# In[33]:


np.random.rand(3,5)
# 2D


# In[39]:


# Returning numbers not from a uniform distribution 0 to 1 instead from a normal distribution centered around zero
#randn
# Gaussian distribution curve
np.random.randn(3)


# In[41]:


np.random.randn(4,4)


# In[44]:


# Random integers from a low to a high number
np.random.randint(1,100)
#low- inclusive and high- exclusive


# In[45]:


np.random.randint(1,100)


# In[46]:


# if you want 10 integers from the range of 1 to 99
np.random.randint(1,100,10)


# In[47]:


arr = np.arange(25)


# In[48]:


arr


# In[51]:


arr.reshape(5,5)


# In[52]:


arr.max()


# In[53]:


arr.min()


# In[54]:


arr.argmax()


# In[55]:


arr.argmin()


# In[57]:


arr.shape


# In[60]:


arr = arr.reshape(5,5)


# In[61]:


arr.shape


# In[62]:


arr.dtype


# In[65]:


from numpy.random import randint
randint(7,10)


# In[ ]:




