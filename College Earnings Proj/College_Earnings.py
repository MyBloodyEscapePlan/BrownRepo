
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


recent_grads = pd.read_csv("recent-grads.csv")
recent_grads.iloc[0]


# In[4]:


recent_grads.head()


# In[5]:


recent_grads.tail()


# In[11]:


raw_data_count = len(recent_grads)
raw_data_count


# In[12]:


recent_grads = recent_grads.dropna()
cleaned_data_count = len(recent_grads)


# In[13]:


cleaned_data_count

