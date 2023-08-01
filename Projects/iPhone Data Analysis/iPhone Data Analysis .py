#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


df = pd.read_csv("apple_products.csv")


# In[4]:


df.head()


# In[5]:


df.count()


# In[7]:


df['Mrp'].max()


# In[8]:


df['Mrp'].min()


# In[9]:


df[df['Mrp'] == 149900]


# In[10]:


df[df['Mrp'] == 39900]


# In[11]:


df[df['Mrp'] >= 100000]


# In[12]:


df[df['Mrp'] <= 100000]


# In[15]:


type(df['Product Name'])


# In[16]:


#convert series into list

list(df['Product Name'])


# In[17]:


list(df['Product Name']) [5]


# In[21]:


list(df['Product Name']) [5].upper()


# In[20]:


list(df['Product Name']) [5].lower()


# In[24]:


list(df['Product Name']) [0][6:15]


# In[30]:


#Remove the space from start and back

list(df['Product Name']) [0][6:15].strip()


# In[31]:


list(df['Product Name']) [54][6:15].strip()


# In[32]:


df['Model Name'] = df['Product Name'].str[6:15]


# In[33]:


df['Model Name']. head()


# In[35]:


df.sort_values(by=['Star Rating'], ascending = False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




