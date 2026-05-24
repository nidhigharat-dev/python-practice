#!/usr/bin/env python
# coding: utf-8

# #### *Map and filter functions*
# ##### *Map creates an iterable function that iterates the values listed*

# In[1]:


def times2(var):
    return var**2
times2(5)


# In[3]:


# Map Function--> gives the address
seq = [1,2,3,4,5]
map(times2,seq)


# In[7]:


# Map Function--> in order to receive the final list, use list function
# Instead of original sequence list [1,2,4,5] we instead receive square of all the list elements
seq = [1,2,3,4,5]
list(map(times2,seq))


# In[11]:


def times2(var) : return var ** 2
times2(5)


# #### *Lamda Expression*
# #### *You can define a function without actually naming it*

# In[12]:


lambda var : var ** 2


# In[16]:


t = lambda var : var ** 2
t(5)


# In[19]:


#num is not defined, everytime the map loop iterates one element from seq list is taken and the calculated value is stored in num

list(map(lambda num: num ** 2, seq))


# #### *Filter Function*

# In[20]:


#Filtering out even numbers without actually defining a function
list(filter(lambda num : num%2 == 0, seq))


# #### *Methods*
# 

# In[28]:


s = ' My name is Nidhi '
# .TAB
s.lower()


# In[29]:


s.split()


# In[38]:


message = 'Go Sports! good play'
message.split()


# In[45]:


# To filter out hashtags from a string
message = 'Go Sports! good play #NICE' #<---We have defined a hashtag here
message.split('#')[1]


# In[46]:


d = {'k1' : 1, 'k2' : 2}


# In[47]:


d


# In[51]:


d.keys()


# In[52]:


d.items()


# In[53]:


d.values()


# #### *To remove the last item from the list*

# In[55]:


lst = [1,2,3]
lst.pop()


# In[57]:


lst # the change is permanent


# In[76]:


new_list = [1,2,3,4,5,6]
test = new_list.pop
test()   #the removed item is stored in assigned function
new_list


# In[77]:


test_2 = new_list.pop(0)
test_2


# In[78]:


new_list


# #### *In Operator*

# In[79]:


'x' in [1,2,3]


# In[80]:


'x' in ['x','y','z']


# #### *Tuple Unpacking*

# In[81]:


x = [(1,2),(3,4),(5,6)]


# In[83]:


x[0][1]


# In[84]:


for a,b in x:
    print(a)


# In[85]:


for a,b in x:
    print(a,b)


# In[87]:


for a,b in x:
    print (b)

