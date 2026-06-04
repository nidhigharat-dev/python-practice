#!/usr/bin/env python
# coding: utf-8

# ___
# 
# <a href='http://www.pieriandata.com'> <img src='../Pierian_Data_Logo.png' /></a>
# ___

# # NumPy Exercises 
# 
# Now that we've learned about NumPy let's test your knowledge. We'll start off with a few simple tasks, and then you'll be asked some more complicated questions.

# #### Import NumPy as np

# use print to print down strings

# #### Create an array of 10 zeros 

# In[3]:


import numpy as np
array = np.zeros(10)
array


# In[ ]:





# #### Create an array of 10 ones

# In[18]:


new_array = np.ones(10)
new_array


# #### Create an array of 10 fives

# In[19]:


nnew_array = np.ones(10)*5
nnew_array


# In[ ]:





# #### Create an array of the integers from 10 to 50

# In[20]:


rarray = np.arange(10,51)
rarray


# #### Create an array of all the even integers from 10 to 50

# In[23]:


even_array = np.arange(10,51,2)
even_array


# #### Create a 3x3 matrix with values ranging from 0 to 8

# In[24]:


np.arange(9).reshape(3,3)


# #### Create a 3x3 identity matrix

# In[25]:


np.eye(3)


# #### Use NumPy to generate a random number between 0 and 1

# In[35]:


np.random.rand(1)


# #### Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution

# In[37]:


normal_distribution = np.random.randn(25)
normal_distribution 


# #### Create the following matrix:

# In[42]:


create = np.arange(1,101).reshape(10,10)/100
create


# #### Create an array of 20 linearly spaced points between 0 and 1:

# In[43]:


new_array = np.linspace(0,1,20)
new_array


# ## Numpy Indexing and Selection
# 
# Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:

# In[44]:


mat = np.arange(1,26).reshape(5,5)
mat


# In[52]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE
mat[2:,1:]


# In[58]:


mat[3:4,4:]


# In[59]:


mat[3,4]


# In[46]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[ ]:





# In[47]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[ ]:





# In[48]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[ ]:





# In[49]:


# WRITE CODE HERE THAT REPRODUCES THE OUTPUT OF THE CELL BELOW
# BE CAREFUL NOT TO RUN THE CELL BELOW, OTHERWISE YOU WON'T
# BE ABLE TO SEE THE OUTPUT ANY MORE


# In[ ]:





# ### Now do the following

# #### Get the sum of all the values in mat

# In[60]:


mat.sum()


# #### Get the standard deviation of the values in mat

# In[61]:


mat.std()


# #### Get the sum of all the columns in mat

# In[62]:


mat.sum(axis=0)


# # Great Job!
