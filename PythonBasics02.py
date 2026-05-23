#!/usr/bin/env python
# coding: utf-8

# #### *Loops*
# ##### *for/while*
# ##### *for- allow to itterate for a sequence*

# In[5]:


nidhi = ['pink', 'blue', 'green','black']
for dress in nidhi:
    print(dress)


# In[7]:


nidhi = ['pink', 'blue', 'green','black']
for dress in nidhi:
    print('no money')


# #### *Loops*
# ##### *while- to continuely perform an action until a condition has been met, executes some block od code while some condition happens to be true*

# In[11]:


i = 1

while i < 5:
    print('i is less than {}'.format(i))
    i = i + 1


# #### *Range*
# ##### *generator of numerical value*

# In[13]:


x = {0,1,2,3,4,5,6,7,8}
for x in range(0,5):
    print(x)


# In[14]:


list(range(0,5))


# In[15]:


list(range(10))


# #### *Appending value to a list*

# In[16]:


x = [1,2,3,4]
out = [] #empty list

for numbers in x:
    out.append(numbers**2)
print(out)    



# In[20]:


[numbers**2 for numbers in x]


# #### *Functions*

# In[36]:


def my_funct(name):
    print('Hello'+ name)
my_funct(' Nidhi')


# #### *Setting a default value/name*
# #### *When printing something, you are going to return or save the variable*

# In[42]:


def my_funct(name = ' Ivy'):
    print('Hello'+ name)
my_funct()


# In[51]:


def my_funct(name = ' Ivy'):
    print('Hello'+ name)
my_funct(' Unni')


# #### *Returning a variable*
# #### *Unlike printing, we have to set it equal to something*
# ##### *Documentary String (DocString--> Documents the function of a string) , No comma in between, Anytime you call a function back and press Shift+Tab, it will tell the purpose of the function*

# In[55]:


def square(num):
    """
    Returns the square of a number.
    """

    return num ** 2
output = square(2)
output


# In[56]:


output = square
output


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




