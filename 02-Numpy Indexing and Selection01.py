#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
arr = np.arange(0,11)
arr


# In[5]:


arr[8]


# In[6]:


arr[1:5]


# In[7]:


arr[:6]


# In[8]:


arr[5:]


# In[10]:


arr[0:5] = 100
arr


# In[11]:


arr[0:5] = 200


# In[12]:


arr # replaces 0 to 5 indexing elements value in array with 200


# In[14]:


slice_of_array = arr[0:6]
slice_of_array


# In[16]:


#Broadcast an array
slice_of_array[:]=99
slice_of_array


# In[17]:


arr #also occurs on original array


# In[21]:


arr_copy = arr.copy()
arr


# In[22]:


arr_copy


# In[23]:


arr_copy[:] = 100


# In[24]:


arr_copy


# In[33]:


arr_2D = np.array([[2,3,4],[5,6,289],[3,6,7]])
arr_2D


# In[44]:


# [start:end]for rows,[start:end]for columns
arr_2D[:2,:2]


# In[48]:


arr_2D[1:,:2]


# In[47]:


# everything upto row __ and column __ onwards
arr_2D[:2,1:]


# In[34]:


arr_2D[1][0]


# In[35]:


arr_2D[2]


# In[37]:


arr_2D[1][2]


# In[39]:


# or
arr_2D[1,2]


# In[54]:


prac_array = np.linspace(2,40,20)
prac_array


# In[58]:


prac_arr = np.random.rand(2,40)
prac_arr


# In[59]:


new_arr = np.random.randint(1,20,size = (6,6))
new_arr


# In[74]:


new_arr[3:,:4]


# In[66]:


new_arr[3:,3:]


# #### *Conditional Selection*

# In[77]:


arr = np.arange(0,11)
arr


# In[78]:


arr > 5


# In[80]:


result = arr > 5
arr[result]


# In[81]:


arr[arr>5]


# In[83]:


arr_2D = np.arange(50).reshape(5,10)
arr_2D


# In[84]:


arr_2D[2:4,6:8]


# In[ ]:




