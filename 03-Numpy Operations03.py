#!/usr/bin/env python
# coding: utf-8

# ## **Numpy Operations**
# #### *Array with Array*
# #### *Array with Scalars*
# #### *Universal Array Functions*

# In[3]:


import numpy as np
arr = np.arange(0,11)
arr


# #### *Array with Array*

# In[4]:


arr + arr # elements to elements basis


# In[5]:


arr - arr


# In[6]:


arr * arr


# In[7]:


arr + 100


# In[8]:


arr * 100


# In[9]:


arr - 100


# In[10]:


1/0


# In[11]:


arr / arr # warning is given null object


# In[13]:


1 / arr # inf signifies infinity


# In[14]:


arr ** 2


# In[16]:


np.sqrt(arr) #taking square root of every element in the array


# In[17]:


np.exp(arr)


# In[18]:


np.max(arr)


# In[19]:


np.min(arr)


# In[20]:


np.sin(arr)


# In[21]:


np.log(arr)


# In[ ]:




