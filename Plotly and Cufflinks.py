#!/usr/bin/env python
# coding: utf-8

# In[24]:


import chart_studio.plotly as py
pd.options.plotting.backend = "plotly"
import pandas as pd
import numpy as np
from plotly import __version__
print(__version__)
get_ipython().run_line_magic('matplotlib', 'inline')


# In[25]:


import cufflinks as cf
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot


# In[26]:


init_notebook_mode(connected=True)


# In[27]:


cf.go_offline()


# In[28]:


#DATA
df = pd.DataFrame(np.random.rand(100,4),columns='A B C D'.split())


# In[29]:


df


# In[30]:


df2 = pd.DataFrame({'Category':['A', 'B','C'],'Values':[32,43,50]})


# In[31]:


df2


# In[34]:


import cufflinks as cf
import plotly
import numpy as np

print(cf.__version__)
print(plotly.__version__)
print(np.__version__)


# In[40]:


import plotly.express as px

px.line(df)


# In[51]:


px.scatter(data_frame=df,x='A',y='B')


# In[55]:


px.bar(data_frame=df2,x='Category',y='Values')


# In[56]:


df


# In[59]:


px.bar(data_frame=df)


# In[62]:


px.box(data_frame=df)


# In[64]:


df3 = pd.DataFrame({'x':[1,2,3,4,5],'y':[10,20,30,20,10],'z':[500,400,300,200,100]})


# In[65]:


df3


# In[69]:


import plotly.graph_objects as go


# In[75]:


go.Figure(data=[ go.Surface(z=df3.values)])


# In[86]:


px.histogram(data_frame=df

            )


# In[85]:


px.histogram(data_frame=df,x=['A'])


# In[94]:


px.violin(data_frame=df)


# In[97]:


px.scatter_matrix(data_frame=df,title='Nice')


# In[ ]:




