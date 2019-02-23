
# coding: utf-8

# In[1]:


import pandas as pd

cpi_df = pd.read_csv(r"C:\Users\Michael\Documents\CSV Files\CPI_By_State.csv")
cpi_df.head()


# In[2]:


cpi_df.shape


# For what we want to do, we only care about the first column (100% Composite Index). Let's make a dictionary where all of the keys are the cities and all of the values are each city's respective 100% CPI.

# In[3]:


cols = ['Urban Area', '100% Composite Index']
cpi_df = cpi_df[cols]
cpi_df.head()


# In[4]:


cpi_df.dropna()


# In[5]:


cpi_dict = {}
urban_areas = cpi_df['Urban Area']
cpi_series = cpi_df['100% Composite Index']


# In[10]:


urban_areas[0]


# In[11]:


cpi_series[0]


# In[6]:


length = len(cpi_series)
for idx in range(0,length):
    cpi_dict[urban_areas[idx]] = cpi_series[idx]


# In[7]:


cpi_dict


# In[8]:


def equivalent_income(current_state, new_state, current_income):
    equiv_income = current_income * (cpi_dict[new_state]/cpi_dict[current_state])
    return equiv_income


# In[9]:


san_fran_income = equivalent_income("Troy-Miami, County, OH", "San, Francisco, CA", 50000 )
san_fran_income


# I knew the cost of living was insane in San Fran but geez. Regarding the dataset, some of the states have more commas than necessary. The very first state in the dataset doesn't have a comma at all. This incongruence makes using the equivalent income function a bit of an annoyance. Let's set all the states to the same format. 

# In[ ]:


Link to dataset: https://www2.census.gov/library/publications/2011/compendia/statab/131ed/tables/12s0728.xls


# In[20]:


cpi_df['Urban Area'] = cpi_df['Urban Area'].str.replace(",", "")
urban_areas = cpi_df['Urban Area']


# In[21]:


length = len(cpi_series)
cpi_dict = {}
for idx in range(0,length):
    cpi_dict[urban_areas[idx]] = cpi_series[idx]


# In[22]:


cpi_dict


# In[23]:


columbus_income = equivalent_income("Troy-Miami County OH", "Columbus OH", 50000)
columbus_income


# I found this interesting. I assumed that the cost of living in Columbus would be greater than that of Troy. This dataset is from 2011, so things could have changed. Let's compare the CPIs of the two areas.

# In[24]:


cpi_dict["Troy-Miami County OH"]


# In[25]:


cpi_dict["Columbus OH"]


# So the CPI for Columbus is indeed lower than the one for Troy. As stated before, this dataset is from 2011. I'll look into finding a more up-to-date dataset in the future. For now, we can play around with the function.

# In[27]:


columbia_income = equivalent_income("Troy-Miami County OH", "Columbia SC", 50000)
columbia_income

