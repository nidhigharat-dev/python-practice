#!/usr/bin/env python
# coding: utf-8

# ### **Creating Dictionaries: {'key':'value'}** 
# #### *behave like key, value pairs like hash tables instead of holding elements through sequence, they hold elements through keys and their actual values*
# 

# In[9]:


d = {'sobo': {'nidhi':'06022002','VAT':[14072002, 29042002]}}


# #### *Using lists under dictionaries*

# In[11]:


d['sobo']


# In[12]:


d['sobo']['VAT']


# In[13]:


d['sobo']['VAT'][0]


# ### **Tuples**
# #### *Very similar to lists, instead of square brackets we use paranthesis ()*

# In[14]:


nidhi = ('sobo', 'ivy','unni')


# In[19]:


nidhi[1]


# #### *Tuples are immutable: they do not let change the assigned data*
# ##### *Lists are mutable, they let you change objects inside the list*
# 

# In[22]:


nidhi[1]= 'chappri'


# #### *SETS: collection of unique entries*
# ##### *They are only defined by unique elements out of repeated ones*
# ##### *to add elements to tuple use .add*

# In[20]:


{'sobo','sobo','unni','unni','ivy'}


# #### **Comparison Operators**
# ##### *Boolean*

# In[25]:


1 > 2


# ##### *Equality*

# In[27]:


1 == 2


# ##### *Inequality*

# In[28]:


1 != 2


# In[29]:


'hi' == 'bye'


# In[31]:


'hi' == 'hi'


# ##### *Logical Operators*
# ###### *AND/OR*

# In[32]:


1 < 2 and 2 > 3


# In[33]:


1 < 2 and 2 < 3


# ##### *You can wrap the statements in paranthesis () so that they are readable*

# In[34]:


( 1 < 2 ) and ( 2 < 3 )


# In[37]:


( 1 < 2 ) or ( 2 > 3 ) or (1 == 1)


# ##### *CodeBlocks: if, if/else, else*
# ##### *Uses indentation*

# In[38]:


if True:
    x = 2 + 2


# In[42]:


x


# #### *ELIF---Checks Multiple Conditions*

# In[45]:


if 1 == 2:
    print('PASS')
elif 3 == 3:
    print('MODERATE')
else:
    print('FAIL')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




