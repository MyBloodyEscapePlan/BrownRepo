
# coding: utf-8

# In[1]:


import pandas as pd

star_wars = pd.read_csv('star_wars.csv', encoding="ISO-8859-1")
star_wars.head(10)


# In[2]:


star_wars.shape


# In[3]:


resp_bool = star_wars['RespondentID'].notnull()
star_wars = star_wars[resp_bool]
star_wars.head(10)


# In[4]:


star_wars.shape


# In[5]:


yes_no = {
    'Yes': True,
    'No': False
}
star_wars['Seen Star Wars?'] = star_wars['Have you seen any of the 6 films in the Star Wars franchise?']
star_wars['Star Wars Fan?'] = star_wars['Do you consider yourself to be a fan of the Star Wars film franchise?']

star_wars['Seen Star Wars?'] = star_wars['Seen Star Wars?'].map(yes_no)
star_wars['Star Wars Fan?'] = star_wars['Star Wars Fan?'].map(yes_no)


# In[6]:


star_wars['Seen Star Wars?'] 


# In[7]:


star_wars['Star Wars Fan?'] 


# In[8]:


old_cols = star_wars.columns[3:9]
new_cols = {}

old_cols


# In[9]:


new_num = 1
for col in old_cols:
    new_cols[col] = "seen_" + str(new_num)
    new_num += 1

new_cols


# In[10]:


star_wars = star_wars.rename(columns = new_cols)
star_wars.head(10)


# In[11]:


def Star_Wars_bool(string):
    sub_string = "Star Wars"
    if sub_string not in string:
        return False
    return True


# In[12]:


cols = star_wars.columns[3:9]

for col in cols:
    star_wars[col] = star_wars[col].fillna('No')
    star_wars[col] = star_wars[col].apply(Star_Wars_bool)


# In[13]:


star_wars.head(10)


# In[14]:


star_wars.columns[9:15]


# In[15]:


rank_cols = star_wars.columns[9:15]
star_wars[rank_cols] = star_wars[rank_cols].astype(float)
new_rank_cols = {}

new_num_0 = 1
for col in rank_cols:
    new_rank_cols[col] = "ranking_" + str(new_num_0)
    new_num_0 += 1

new_rank_cols


# In[16]:


star_wars = star_wars.rename(columns = new_rank_cols)
star_wars.columns[9:15]


# In[17]:


get_ipython().run_line_magic('matplotlib', 'inline')

star_wars_mean = star_wars.mean()
star_wars_mean


# In[18]:


rankings = star_wars_mean[7:13]
rankings


# In[19]:


rankings.plot.bar()


# Ranking 5 (Empire Strikes Back) has the lowest (best) score of the films. Return of the Jedi and A New Hope (rankings 4 and 6, respectively) are neck-and-neck. The new trilogy was overall worse rated than the OG.

# In[20]:


star_wars_sum = star_wars.sum()
star_wars_sum


# In[21]:


seen_sums = star_wars_sum[2:8]
seen_sums


# In[22]:


seen_sums.plot.bar()


# It seems that Empire is the most seen of all 6 films, which would indeed help its ranking. Return of the Jedi had almost as much viewership, but its ranking is visibly worse than Empire's. That gives insight to the slightly negative reaction to Return of the Jedi. 
# 
# Revenge of the Sith is the least seen of the movies, which explains it having the worst ranking. It seems like viewership for the new trilogy dropped successively.

# In[24]:


males = star_wars[star_wars["Gender"] == "Male"]
females = star_wars[star_wars["Gender"] == "Female"]
males.head()


# In[25]:


females.head()


# In[26]:


males_mean = males.mean()
males_mean


# In[27]:


male_rankings = males_mean[7:13]
male_rankings


# In[28]:


male_rankings.plot.bar()


# In[30]:


male_sum = males.sum()
males_seen = male_sum[2:8] 
males_seen


# In[31]:


males_seen.plot.bar()


# In[32]:


females_mean = females.mean()
female_rankings = females_mean[7:13]
female_rankings.plot.bar()


# In[33]:


female_sum = females.sum()
females_seen = female_sum[2:8]
females_seen.plot.bar()


# While a greater magnitude of respondents who saw the movie are men, the viewership and ranking distributions are similar for both genders.
