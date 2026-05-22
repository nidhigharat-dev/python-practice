#!/usr/bin/env python
# coding: utf-8

# Python Datatypes:
# 1. Integer

# In[1]:


1


# 2. Floating

# In[2]:


1.0


# ADDITION

# In[3]:


1 + 1


# MULTIPLICATION

# In[4]:


1 * 1


# DIVISION

# In[5]:


1 / 2


# EXPONENTS

# In[6]:


2 ** 4


# Order of calculations: multiplication first then addition

# In[7]:


2 + 3 * 5 + 5


# USE PARANTHESIS TO CLARIFY YOUR ORDER

# In[8]:


(2+3) * (5+5)


# Modulus (mod function)- returns what remains after the division- to check if the numbers are even

# In[9]:


4 % 2


# Creating Variable- use (=) operator, shouldnt start with numbers, cannot start with special characters, will update each time it is called

# In[10]:


x = 2
y = 3


# In[11]:


x + y


# In[12]:


x = x + x
x


# Strings ''   "" to print a string use print("")

# In[13]:


num = 23
name = 'nidhi'


# In[19]:


print('My name is {} and my age is {}'.format(name,num))


# In[26]:


print('My name is {one} and my age is {zero}, Ivy and VAT loves {one}'.format(zero=num,one=name))


# Indexing Strings: starts from zero

# In[30]:


s = 'sobohatesskobo'


# In[31]:


s[10]


# Slicing of Indexing

# In[33]:


s[4:9]


# Lists : sequence of elements [,] can takeup any data type
# if any element is further added to the list use .append
# just like string, it is also a sequence

# In[34]:


my_list = ['nidhi', 'sobo', 'ivy', 'dukkar']


# In[35]:


my_list.append('genda')


# In[36]:


my_list


# In[38]:


my_list[1:3]


# Replacing the original item in the list

# In[39]:


my_list[3] = 'morni'


# In[40]:


my_list


# Nesting of strings

# In[47]:


nest = ['nidhi', 'ivy', ['genda', 'sobo',['chimni']]]


# In[48]:


nest[2]


# In[49]:


nest[2][2]


# In[50]:


nest[2][2][0]


# In[52]:


print(nest[2][2][0])


# In[ ]:




