
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

mental_df = pd.read_csv(r"C:\Users\Michael\Documents\CSV Files\survey.csv")
mental_df.head(10)


# In[2]:


mental_df.shape


# Since we want info on employees who are exclusively in the tech industry, let's filter out rows where tech_company is 'Yes'. 

# In[3]:


tech_bool = mental_df['tech_company'] == 'Yes'
mental_df = mental_df[tech_bool]


# In[4]:


gender_labels = mental_df['Gender'].unique()
gender_labels


# In[5]:


male_labels = ['M', 'ostensibly male', 'Male', 'male', 'm', 'maile', 'Mal', 'Male (CIS)', 'Male ', 'Man', 'Mail', 'cis male', 'Malr', 'Cis Man', 'Cis Male', 'msle']
female_labels = ['F', 'Female', 'female', 'Cis Female', 'f', 'Femake', 'woman', 'cis-female/femme', 'Female (cis)', 'femail']


# In[6]:


def clean_gender(string):
    if string in male_labels:
        string = 'M'
    elif string in female_labels:
        string = 'F'
    else:
        string = 'Q'
    return string


# In[7]:


mental_df['Gender'] = mental_df['Gender'].apply(clean_gender)
mental_df['Gender']


# In[8]:


mental_df['Gender'].describe()


# In[9]:


mental_df['Gender'].value_counts().plot(kind='barh')


# Representation in the tech industry is extremely cis male. Queer people make up a marginal portion of workers in the tech industry.

# In[10]:


mental_df['Gender'].value_counts()


# In[11]:


mental_df['Age'].dtype    


# In[12]:


mental_df['Age'][0:10]


# In[13]:


mental_df['Age'].describe()


# There seems to be a huge outlier skewing the data. Let's remove that.

# In[14]:


mental_df['Age'].dtype


# In[15]:


age_grt_than = mental_df['Age'] > 15
age_lss_than = mental_df['Age'] < 100
age_bool = age_grt_than & age_lss_than
mental_df = mental_df[age_bool]


# In[16]:


mental_df['Age'].dtype


# In[17]:


mental_df['Age'].describe()


# In[18]:


mental_df['Age'].hist()


# The distribution for employee age in the tech industry is right-skewed. The majority of employees are between 20 and 40 years old. Those who are 50 and above are most likely top-level executives and/or CEOs.

# For the following analyses, I will split the dataset by gender (male and female). The queer population will be omitted for the time being, since they make up less than 5% of employees. We will come back to them shortly. 
# 
# Since the male population dwarfs the female population by a factor of 4, we will randomly select 100 employees from both genders. Once we have our two dataframes, we can start exploring.
# 
# But first, let's clean up the dataframe we have now.

# In[19]:


mental_df.info()


# State, work_interfere, and comments have high percentages of missing values (41%, 20%, and 87% respectively). These columns will not add to the analysis, so we will drop them. 

# In[20]:


drop_cols = ['state', 'work_interfere', 'comments']
mental_df = mental_df.drop(drop_cols, axis=1)
mental_df.head()


# self_employed only has 18 rows (1.4%) of missing values. We can drop these rows. 

# In[21]:


mental_df = mental_df.dropna()
mental_df.head()


# In[22]:


mental_df.shape


# Now let's split the dataset by male and female.

# In[23]:


male_bool = mental_df['Gender'] == 'M'
all_male_df = mental_df[male_bool]
all_male_df.shape


# In[24]:


female_bool = mental_df['Gender'] == 'F'
all_female_df = mental_df[female_bool]
all_female_df.shape


# Now let's randomly select 100 rows from each dataframe. 

# In[25]:


sample_male_df = all_male_df.sample(100)
sample_male_df.shape


# In[26]:


sample_male_df.head(10)


# In[27]:


sample_female_df = all_female_df.sample(100)
sample_female_df.shape


# In[28]:


sample_female_df.head(10)


# Let's compare the age distributions of male and female employees in the tech industry.

# In[29]:


sample_male_df['Age'].hist()


# In[30]:


sample_female_df['Age'].hist()


# Both distributions are right-skewed. The male distribution has a 10-year wider range, the oldest employees being in their 50s while the oldest female employees are in their 40s. Besides that, the distributions seem very similar.
# 
# Next, let's compare the percentage of men and women who sought treatment for a mental health condition.

# In[31]:


treatment_map = {
    'Yes': True,
    'No': False
}

sample_male_df['treatment'] = sample_male_df['treatment'].map(treatment_map)
sample_male_df.head(10)


# In[32]:


sample_female_df['treatment'] = sample_female_df['treatment'].map(treatment_map)
sample_female_df.head(10)


# In[33]:


num_male_treatment = sample_male_df['treatment'].sum()
num_female_treatment = sample_female_df['treatment'].sum()


# In[39]:


plt.bar(['Male', 'Female'], [num_male_treatment, num_female_treatment])
plt.show()


# It seems like more female employees have sought treatment for mental conditions than male employees. Now let's see how easy it is for employees to take leave for mental health reasons. 

# In[42]:


sample_male_df['leave'].value_counts().plot(kind='barh')


# In[43]:


sample_female_df['leave'].value_counts().plot(kind='barh')

