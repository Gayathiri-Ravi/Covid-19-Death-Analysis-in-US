#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from IPython import get_ipython
import warnings
warnings.filterwarnings("ignore")


# In[2]:


data1 = pd.read_csv('g1.csv')
data2 = pd.read_csv('g2.csv')


# In[3]:


data1.head()


# In[4]:


data1.tail()


# In[5]:


data1 = data1.dropna()


# In[6]:


data1 = data1.drop('Unnamed: 0', axis = 1)


# In[7]:


data1.shape


# In[8]:


data1.columns


# In[9]:


data1.duplicated().sum()


# In[10]:


data1.isnull().sum()


# In[11]:


data1.info()


# In[12]:


data1.describe()


# In[13]:


data2.head()


# In[14]:


data2.tail()


# In[15]:


data2 = data2.dropna()


# In[16]:


data2 = data2.drop('Unnamed: 0', axis = 1)


# In[17]:


data2.shape


# In[18]:


data2.columns


# In[19]:


data2.duplicated().sum()


# In[20]:


data2.isnull().sum()


# In[21]:


data2.info()


# In[22]:


data2.describe()


# In[23]:


data3 = data2.copy()


# In[24]:


data3['date'] = pd.to_datetime(data3['date'])


# In[25]:


data3.head()


# In[26]:


data3['month'] = pd.DatetimeIndex(data3['date']).month


# In[27]:


data3.head()


# In[28]:


data3 = data3.sort_values(by='month', ascending = False)


# In[29]:


data3.head()


# In[30]:


data_march= data3[data3['month'] == 3]


# In[31]:


data_march.nunique()


# In[32]:


data_march.shape


# In[33]:


data_march['deaths'].sum()


# In[34]:


data_march.to_csv('data_march.csv')


# In[35]:


data_march_deaths = data_march.groupby('state')['deaths'].sum()


# In[36]:


data_march_deaths


# In[37]:


data_march_deaths = pd.DataFrame(data_march_deaths)


# In[38]:


data_march_deaths.head()


# In[39]:


data_march_deaths = data_march_deaths.reset_index()


# In[40]:


data_march_deaths.head()


# In[41]:


top_data_march_deaths = data_march_deaths.sort_values(by=['deaths'], 
                                                      ascending = False)


# In[42]:


top_data_march_deaths.head()


# In[43]:


plt.figure(figsize=(15,6))
sns.barplot(x = 'state' , y = 'deaths', data = top_data_march_deaths.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[44]:


plt.figure(figsize=(15,6))
sns.lineplot(x = 'state' , y = 'deaths', data = top_data_march_deaths.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[45]:


plt.figure(figsize=(15,6))
sns.histplot(x = 'state' , y = 'deaths', data = top_data_march_deaths.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[46]:


plt.figure(figsize=(15,6))
sns.scatterplot(x = 'state' , y = 'deaths', data = top_data_march_deaths.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[47]:


#top 3 deaths state are: 
# 1. New York 
# 2. New Jersey 
# 3. Massachusetts


# In[48]:


data_april= data3[data3['month'] == 4]


# In[49]:


data_april.nunique()


# In[50]:


data_april.shape


# In[51]:


data_april['deaths'].sum()


# In[52]:


data_april.to_csv('data_april.csv')


# In[53]:


data_april_deaths = data_april.groupby('state')['deaths'].sum()


# In[54]:


data_april_deaths


# In[55]:


data_april_deaths = pd.DataFrame(data_april_deaths)


# In[56]:


data_april_deaths.head()


# In[57]:


data_april_deaths = data_march_deaths.reset_index()


# In[58]:


data_april_deaths.head()


# In[59]:


top_data_april_deaths = data_april_deaths.sort_values(by=['deaths'], 
                                                      ascending = False)


# In[60]:


top_data_april_deaths.head()


# In[61]:


plt.figure(figsize=(15,6))
sns.barplot(x = 'state' , y = 'deaths', data = top_data_april_deaths.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[62]:


plt.figure(figsize=(15,6))
sns.lineplot(x = 'state' , y = 'deaths', data = top_data_april_deaths.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[63]:


plt.figure(figsize=(15,6))
sns.histplot(x = 'state' , y = 'deaths', data = top_data_april_deaths.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[64]:


plt.figure(figsize=(15,6))
sns.scatterplot(x = 'state' , y = 'deaths', data = top_data_april_deaths.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[65]:


#top 3 deaths state are: 
# 1. New York 
# 2. New Jersey 
# 3. Massachusetts


# In[66]:


data_may= data3[data3['month'] == 5]


# In[67]:


data_may.nunique()


# In[68]:


data_may.shape


# In[69]:


data_may['deaths'].sum()


# In[70]:


data_may.to_csv('data_may.csv')


# In[71]:


data_may_deaths = data_may.groupby('state')['deaths'].sum()


# In[72]:


data_may_deaths


# In[73]:


data_may_deaths = pd.DataFrame(data_may_deaths)


# In[74]:


data_may_deaths.head()


# In[75]:


data_may_deaths = data_may_deaths.reset_index()


# In[76]:


data_may_deaths.head()


# In[77]:


top_data_may_deaths = data_may_deaths.sort_values(by=['deaths'], 
                                                      ascending = False)


# In[78]:


top_data_may_deaths.head()


# In[79]:


plt.figure(figsize=(15,6))
sns.barplot(x = 'state' , y = 'deaths', data = top_data_may_deaths.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[80]:


plt.figure(figsize=(15,6))
sns.lineplot(x = 'state' , y = 'deaths', data = top_data_may_deaths.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[81]:


plt.figure(figsize=(15,6))
sns.histplot(x = 'state' , y = 'deaths', data = top_data_may_deaths.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[82]:


plt.figure(figsize=(15,6))
sns.scatterplot(x = 'state' , y = 'deaths', data = top_data_may_deaths.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[83]:


#top 3 deaths state are: 
# 1. New York 
# 2. New Jersey 
# 3. Massachusetts


# In[84]:


data_june= data3[data3['month'] == 6]


# In[85]:


data_june.nunique()


# In[86]:


data_june.shape


# In[87]:


data_june['deaths'].sum()


# In[88]:


data_june.to_csv('data_june.csv')


# In[89]:


data_june_deaths = data_june.groupby('state')['deaths'].sum()


# In[90]:


data_june_deaths


# In[91]:


data_june_deaths = pd.DataFrame(data_june_deaths)


# In[92]:


data_june_deaths.head()


# In[93]:


data_june_deaths = data_june_deaths.reset_index()


# In[94]:


data_june_deaths.head()


# In[95]:


top_data_june_deaths = data_june_deaths.sort_values(by=['deaths'], 
                                                      ascending = False)


# In[96]:


top_data_june_deaths.head()


# In[97]:


plt.figure(figsize=(15,6))
sns.barplot(x = 'state' , y = 'deaths', data = top_data_june_deaths.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[98]:


plt.figure(figsize=(15,6))
sns.lineplot(x = 'state' , y = 'deaths', data = top_data_june_deaths.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[99]:


plt.figure(figsize=(15,6))
sns.histplot(x = 'state' , y = 'deaths', data = top_data_june_deaths.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[100]:


plt.figure(figsize=(15,6))
sns.scatterplot(x = 'state' , y = 'deaths', data = top_data_june_deaths.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[101]:


#top 3 deaths state are: 
# 1. New York 
# 2. New Jersey 
# 3. Massachusetts


# In[102]:


data4 = data1.copy()


# In[103]:


data4.head()


# In[104]:


data4['date'] = pd.to_datetime(data4['date'])


# In[105]:


data4.head()


# In[106]:


data4['month'] = pd.DatetimeIndex(data4['date']).month


# In[107]:


data4.head()


# In[108]:


data4 = data4.sort_values(by='month', ascending = False)


# In[109]:


data4.head()


# In[110]:


data_march_new= data4[data4['month'] == 3]


# In[111]:


data_march_new_NY= data_march_new[data_march_new['state_name'] == 'NY']


# In[112]:


data_march_new_NY.head()


# In[113]:


data_march_new_NY.nunique()


# In[114]:


data_march_new_NY_new = data_march_new_NY[['county_name', 'deaths']]


# In[115]:


data_march_new_NY_new.head()


# In[116]:


data_march_new_NY_new['deaths'].sum()


# In[117]:


data_march_new_NY_new.to_csv('data_march_new_NY_new.csv')


# In[118]:


data_march_new_NY_new = data_march_new_NY_new.groupby('county_name')['deaths'].sum()


# In[119]:


data_march_new_NY_new


# In[120]:


data_march_new_NY_new = pd.DataFrame(data_march_new_NY_new)


# In[121]:


data_march_new_NY_new.head()


# In[122]:


data_march_new_NY_new = data_march_new_NY_new.reset_index()


# In[123]:


data_march_new_NY_new.head()


# In[124]:


top_data_march_new_NY_new = data_march_new_NY_new.sort_values(by=['deaths'], 
                                                      ascending = False)


# In[125]:


top_data_march_new_NY_new.head()


# In[126]:


plt.figure(figsize=(15,6))
sns.barplot(x = 'county_name' , y = 'deaths', data = top_data_march_new_NY_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[127]:


plt.figure(figsize=(15,6))
sns.lineplot(x = 'county_name' , y = 'deaths', data = top_data_march_new_NY_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[128]:


plt.figure(figsize=(15,6))
sns.histplot(x = 'county_name' , y = 'deaths', data = top_data_march_new_NY_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[129]:


plt.figure(figsize=(15,6))
sns.scatterplot(x = 'county_name' , y = 'deaths', data = top_data_march_new_NY_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[130]:


#top 3 deaths in NY state County are: 
# 1. Kings County 
# 2. Queens County 
# 3. Bronx County


# In[131]:


data_april_new= data4[data4['month'] == 4]


# In[132]:


data_april_new_NY= data_april_new[data_april_new['state_name'] == 'NY']


# In[133]:


data_april_new_NY.head()


# In[134]:


data_april_new_NY.nunique()


# In[135]:


data_april_new_NY_new = data_april_new_NY[['county_name', 'deaths']]


# In[136]:


data_april_new_NY_new.head()


# In[137]:


data_april_new_NY_new['deaths'].sum()


# In[138]:


data_april_new_NY_new.to_csv('data_april_new_NY_new.csv')


# In[139]:


data_april_new_NY_new = data_april_new_NY_new.groupby('county_name')['deaths'].sum()


# In[140]:


data_april_new_NY_new


# In[141]:


data_april_new_NY_new = pd.DataFrame(data_april_new_NY_new)


# In[142]:


data_april_new_NY_new.head()


# In[143]:


data_april_new_NY_new = data_april_new_NY_new.reset_index()


# In[144]:


data_april_new_NY_new.head()


# In[145]:


top_data_april_new_NY_new = data_april_new_NY_new.sort_values(by=['deaths'], 
                                                      ascending = False)


# In[146]:


top_data_april_new_NY_new.head()


# In[147]:


plt.figure(figsize=(15,6))
sns.barplot(x = 'county_name' , y = 'deaths', data = top_data_april_new_NY_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[148]:


plt.figure(figsize=(15,6))
sns.lineplot(x = 'county_name' , y = 'deaths', data = top_data_april_new_NY_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[149]:


plt.figure(figsize=(15,6))
sns.histplot(x = 'county_name' , y = 'deaths', data = top_data_april_new_NY_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[150]:


plt.figure(figsize=(15,6))
sns.scatterplot(x = 'county_name' , y = 'deaths', data = top_data_april_new_NY_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[151]:


#top 3 deaths in NY state County are: 
# 1. Kings County 
# 2. Queens County 
# 3. Bronx County


# In[152]:


data_may_new= data4[data4['month'] == 5]


# In[153]:


data_may_new_NY= data_may_new[data_may_new['state_name'] == 'NY']


# In[154]:


data_may_new_NY.head()


# In[155]:


data_may_new_NY.nunique()


# In[156]:


data_may_new_NY_new = data_may_new_NY[['county_name', 'deaths']]


# In[157]:


data_may_new_NY_new.head()


# In[158]:


data_may_new_NY_new['deaths'].sum()


# In[159]:


data_may_new_NY_new.to_csv('data_may_new_NY_new.csv')


# In[160]:


data_may_new_NY_new = data_may_new_NY_new.groupby('county_name')['deaths'].sum()


# In[161]:


data_may_new_NY_new


# In[162]:


data_may_new_NY_new = pd.DataFrame(data_may_new_NY_new)


# In[163]:


data_may_new_NY_new.head()


# In[164]:


data_may_new_NY_new = data_may_new_NY_new.reset_index()


# In[165]:


data_may_new_NY_new.head()


# In[166]:


top_data_may_new_NY_new = data_may_new_NY_new.sort_values(by=['deaths'], 
                                                      ascending = False)


# In[167]:


top_data_may_new_NY_new.head()


# In[168]:


plt.figure(figsize=(15,6))
sns.barplot(x = 'county_name' , y = 'deaths', data = top_data_may_new_NY_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[169]:


plt.figure(figsize=(15,6))
sns.lineplot(x = 'county_name' , y = 'deaths', data = top_data_may_new_NY_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[170]:


plt.figure(figsize=(15,6))
sns.histplot(x = 'county_name' , y = 'deaths', data = top_data_may_new_NY_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[171]:


plt.figure(figsize=(15,6))
sns.scatterplot(x = 'county_name' , y = 'deaths', data = top_data_may_new_NY_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[172]:


#top 3 deaths in NY state County are: 
# 1. Kings County 
# 2. Queens County 
# 3. Bronx County


# In[173]:


data_june_new= data4[data4['month'] == 6]


# In[174]:


data_june_new_NY= data_june_new[data_june_new['state_name'] == 'NY']


# In[175]:


data_june_new_NY.head()


# In[176]:


data_june_new_NY.nunique()


# In[177]:


data_june_new_NY_new = data_june_new_NY[['county_name', 'deaths']]


# In[178]:


data_june_new_NY_new.head()


# In[179]:


data_june_new_NY_new['deaths'].sum()


# In[180]:


data_june_new_NY_new.to_csv('data_june_new_NY_new.csv')


# In[181]:


data_june_new_NY_new = data_june_new_NY_new.groupby('county_name')['deaths'].sum()


# In[182]:


data_june_new_NY_new


# In[183]:


data_june_new_NY_new = pd.DataFrame(data_june_new_NY_new)


# In[184]:


data_june_new_NY_new.head()


# In[185]:


data_june_new_NY_new = data_june_new_NY_new.reset_index()


# In[186]:


data_june_new_NY_new.head()


# In[187]:


top_data_june_new_NY_new = data_june_new_NY_new.sort_values(by=['deaths'], 
                                                      ascending = False)


# In[188]:


top_data_june_new_NY_new.head()


# In[189]:


plt.figure(figsize=(15,6))
sns.barplot(x = 'county_name' , y = 'deaths', data = top_data_june_new_NY_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[190]:


plt.figure(figsize=(15,6))
sns.lineplot(x = 'county_name' , y = 'deaths', data = top_data_june_new_NY_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[191]:


plt.figure(figsize=(15,6))
sns.histplot(x = 'county_name' , y = 'deaths', data = top_data_june_new_NY_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[192]:


plt.figure(figsize=(15,6))
sns.scatterplot(x = 'county_name' , y = 'deaths', data = top_data_june_new_NY_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[193]:


#top 3 deaths in NY state County are: 
# 1. Kings County 
# 2. Queens County 
# 3. Bronx County


# In[194]:


data_march_new_NJ= data_march_new[data_march_new['state_name'] == 'NJ']


# In[195]:


data_march_new_NJ.head()


# In[196]:


data_march_new_NJ_new = data_march_new_NJ[['county_name', 'deaths']]


# In[197]:


data_march_new_NJ_new.shape


# In[198]:


data_march_new_NJ_new['deaths'].sum()


# In[199]:


data_march_new_NJ_new.to_csv('data_march_new_NJ_new.csv')


# In[200]:


data_march_new_NJ_new = data_march_new_NJ_new.groupby('county_name')['deaths'].sum()


# In[201]:


data_march_new_NJ_new.head()


# In[202]:


data_march_new_NJ_new = pd.DataFrame(data_march_new_NJ_new)


# In[203]:


data_march_new_NJ_new.head()


# In[204]:


data_march_new_NJ_new = data_march_new_NJ_new.reset_index()


# In[205]:


data_march_new_NJ_new.head()


# In[206]:


top_data_march_new_NJ_new = data_march_new_NJ_new.sort_values(by=['deaths'], 
                                                      ascending = False)


# In[207]:


top_data_march_new_NJ_new.head()


# In[208]:


plt.figure(figsize=(15,6))
sns.barplot(x = 'county_name' , y = 'deaths', data = top_data_march_new_NJ_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[209]:


plt.figure(figsize=(15,6))
sns.lineplot(x = 'county_name' , y = 'deaths', data = top_data_march_new_NJ_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[210]:


plt.figure(figsize=(15,6))
sns.histplot(x = 'county_name' , y = 'deaths', data = top_data_march_new_NJ_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[211]:


plt.figure(figsize=(15,6))
sns.scatterplot(x = 'county_name' , y = 'deaths', data = top_data_march_new_NJ_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[212]:


#top 3 deaths in NJ state County are: 
# 1. Essex County
# 2. Bergen County 
# 3. Hudson County


# In[213]:


data_april_new_NJ= data_april_new[data_april_new['state_name'] == 'NJ']


# In[214]:


data_april_new_NJ.head()


# In[215]:


data_april_new_NJ_new = data_april_new_NJ[['county_name', 'deaths']]


# In[216]:


data_april_new_NJ_new.shape


# In[217]:


data_april_new_NJ_new['deaths'].sum()


# In[218]:


data_april_new_NJ_new.to_csv('data_april_new_NJ_new.csv')


# In[219]:


data_april_new_NJ_new = data_april_new_NJ_new.groupby('county_name')['deaths'].sum()


# In[220]:


data_april_new_NJ_new.head()


# In[221]:


data_april_new_NJ_new = pd.DataFrame(data_april_new_NJ_new)


# In[222]:


data_april_new_NJ_new.head()


# In[223]:


data_april_new_NJ_new = data_april_new_NJ_new.reset_index()


# In[224]:


data_april_new_NJ_new.head()


# In[225]:


top_data_april_new_NJ_new = data_april_new_NJ_new.sort_values(by=['deaths'], 
                                                      ascending = False)


# In[226]:


top_data_april_new_NJ_new.head()


# In[227]:


plt.figure(figsize=(15,6))
sns.barplot(x = 'county_name' , y = 'deaths', data = top_data_april_new_NJ_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[228]:


plt.figure(figsize=(15,6))
sns.lineplot(x = 'county_name' , y = 'deaths', data = top_data_april_new_NJ_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[229]:


plt.figure(figsize=(15,6))
sns.histplot(x = 'county_name' , y = 'deaths', data = top_data_april_new_NJ_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[230]:


plt.figure(figsize=(15,6))
sns.scatterplot(x = 'county_name' , y = 'deaths', data = top_data_april_new_NJ_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[231]:


#top 3 deaths in NJ state County are: 
# 1. Essex County
# 2. Bergen County 
# 3. Hudson County


# In[232]:


data_may_new_NJ= data_may_new[data_may_new['state_name'] == 'NJ']


# In[233]:


data_may_new_NJ.head()


# In[234]:


data_may_new_NJ_new = data_may_new_NJ[['county_name', 'deaths']]


# In[235]:


data_may_new_NJ_new.shape


# In[236]:


data_may_new_NJ_new['deaths'].sum()


# In[237]:


data_may_new_NJ_new.to_csv('data_may_new_NJ_new.csv')


# In[238]:


data_may_new_NJ_new = data_may_new_NJ_new.groupby('county_name')['deaths'].sum()


# In[239]:


data_may_new_NJ_new.head()


# In[240]:


data_may_new_NJ_new = pd.DataFrame(data_may_new_NJ_new)


# In[241]:


data_may_new_NJ_new.head()


# In[242]:


data_may_new_NJ_new = data_may_new_NJ_new.reset_index()


# In[243]:


data_may_new_NJ_new.head()


# In[244]:


top_data_may_new_NJ_new = data_may_new_NJ_new.sort_values(by=['deaths'], 
                                                      ascending = False)


# In[245]:


top_data_may_new_NJ_new.head()


# In[246]:


plt.figure(figsize=(15,6))
sns.barplot(x = 'county_name' , y = 'deaths', data = top_data_may_new_NJ_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[247]:


plt.figure(figsize=(15,6))
sns.lineplot(x = 'county_name' , y = 'deaths', data = top_data_may_new_NJ_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[248]:


plt.figure(figsize=(15,6))
sns.histplot(x = 'county_name' , y = 'deaths', data = top_data_may_new_NJ_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[249]:


plt.figure(figsize=(15,6))
sns.scatterplot(x = 'county_name' , y = 'deaths', data = top_data_may_new_NJ_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[250]:


#top 3 deaths in NJ state County are: 
# 1. Essex County
# 2. Bergen County 
# 3. Hudson County


# In[251]:


data_june_new_NJ= data_june_new[data_june_new['state_name'] == 'NJ']


# In[252]:


data_june_new_NJ.head()


# In[253]:


data_june_new_NJ_new = data_june_new_NJ[['county_name', 'deaths']]


# In[254]:


data_june_new_NJ_new.shape


# In[255]:


data_june_new_NJ_new['deaths'].sum()


# In[256]:


data_june_new_NJ_new.to_csv('data_june_new_NJ_new.csv')


# In[257]:


data_june_new_NJ_new = data_june_new_NJ_new.groupby('county_name')['deaths'].sum()


# In[258]:


data_june_new_NJ_new.head()


# In[259]:


data_june_new_NJ_new = pd.DataFrame(data_june_new_NJ_new)


# In[260]:


data_june_new_NJ_new.head()


# In[261]:


data_june_new_NJ_new = data_june_new_NJ_new.reset_index()


# In[262]:


data_june_new_NJ_new.head()


# In[263]:


top_data_june_new_NJ_new = data_june_new_NJ_new.sort_values(by=['deaths'], 
                                                      ascending = False)


# In[264]:


top_data_june_new_NJ_new.head()


# In[265]:


plt.figure(figsize=(15,6))
sns.barplot(x = 'county_name' , y = 'deaths', data = top_data_june_new_NJ_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[266]:


plt.figure(figsize=(15,6))
sns.lineplot(x = 'county_name' , y = 'deaths', data = top_data_june_new_NJ_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[267]:


plt.figure(figsize=(15,6))
sns.histplot(x = 'county_name' , y = 'deaths', data = top_data_june_new_NJ_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[268]:


plt.figure(figsize=(15,6))
sns.scatterplot(x = 'county_name' , y = 'deaths', data = top_data_june_new_NJ_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[269]:


#top 3 deaths in NJ state County are: 
# 1. Essex County
# 2. Bergen County 
# 3. Hudson County


# In[270]:


data_march_new_MA= data_march_new[data_march_new['state_name'] == 'MA']


# In[271]:


data_march_new_MA.head()


# In[272]:


data_march_new_MA_new = data_march_new_MA[['county_name', 'deaths']]


# In[273]:


data_march_new_MA_new.head()


# In[274]:


data_march_new_MA_new.shape


# In[275]:


data_march_new_MA_new['deaths'].sum()


# In[276]:


data_march_new_MA_new.to_csv('data_march_new_MA_new.csv')


# In[277]:


data_march_new_MA_new = data_march_new_MA_new.groupby('county_name')['deaths'].sum()


# In[278]:


data_march_new_MA_new.head()


# In[279]:


data_march_new_MA_new = pd.DataFrame(data_march_new_MA_new)


# In[280]:


data_march_new_MA_new.head()


# In[281]:


data_march_new_MA_new = data_march_new_MA_new.reset_index()


# In[282]:


data_march_new_MA_new.head()


# In[283]:


top_data_march_new_MA_new = data_march_new_MA_new.sort_values(by=['deaths'], 
                                                      ascending = False)


# In[284]:


top_data_march_new_MA_new.head()


# In[285]:


plt.figure(figsize=(15,6))
sns.barplot(x = 'county_name' , y = 'deaths', data = top_data_march_new_MA_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[286]:


plt.figure(figsize=(15,6))
sns.lineplot(x = 'county_name' , y = 'deaths', data = top_data_march_new_MA_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[287]:


plt.figure(figsize=(15,6))
sns.histplot(x = 'county_name' , y = 'deaths', data = top_data_march_new_MA_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[288]:


plt.figure(figsize=(15,6))
sns.scatterplot(x = 'county_name' , y = 'deaths', data = top_data_march_new_MA_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[289]:


# top 3 deaths in MA state County are: 
# 1. Middlesex County
# 2. Essex County 
# 3. Suffolk County


# In[290]:


data_april_new_MA= data_april_new[data_april_new['state_name'] == 'MA']


# In[291]:


data_april_new_MA.head()


# In[292]:


data_april_new_MA_new = data_april_new_MA[['county_name', 'deaths']]


# In[293]:


data_april_new_MA_new.head()


# In[294]:


data_april_new_MA_new.shape


# In[295]:


data_april_new_MA_new['deaths'].sum()


# In[296]:


data_april_new_MA_new.to_csv('data_april_new_MA_new.csv')


# In[297]:


data_april_new_MA_new = data_april_new_MA_new.groupby('county_name')['deaths'].sum()


# In[298]:


data_april_new_MA_new.head()


# In[299]:


data_april_new_MA_new = pd.DataFrame(data_april_new_MA_new)


# In[300]:


data_april_new_MA_new.head()


# In[301]:


data_april_new_MA_new = data_april_new_MA_new.reset_index()


# In[302]:


data_april_new_MA_new.head()


# In[303]:


top_data_april_new_MA_new = data_april_new_MA_new.sort_values(by=['deaths'], 
                                                      ascending = False)


# In[304]:


top_data_april_new_MA_new.head()


# In[305]:


plt.figure(figsize=(15,6))
sns.barplot(x = 'county_name' , y = 'deaths', data = top_data_april_new_MA_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[306]:


plt.figure(figsize=(15,6))
sns.lineplot(x = 'county_name' , y = 'deaths', data = top_data_april_new_MA_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[307]:


plt.figure(figsize=(15,6))
sns.histplot(x = 'county_name' , y = 'deaths', data = top_data_april_new_MA_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[308]:


plt.figure(figsize=(15,6))
sns.scatterplot(x = 'county_name' , y = 'deaths', data = top_data_april_new_MA_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[309]:


# top 3 deaths in MA state County are: 
# 1. Middlesex County
# 2. Essex County 
# 3. Suffolk County


# In[310]:


data_may_new_MA= data_may_new[data_may_new['state_name'] == 'MA']


# In[311]:


data_may_new_MA.head()


# In[312]:


data_may_new_MA_new = data_may_new_MA[['county_name', 'deaths']]


# In[313]:


data_may_new_MA_new.head()


# In[314]:


data_may_new_MA_new.shape


# In[315]:


data_may_new_MA_new['deaths'].sum()


# In[316]:


data_may_new_MA_new.to_csv('data_may_new_MA_new.csv')


# In[317]:


data_may_new_MA_new = data_may_new_MA_new.groupby('county_name')['deaths'].sum()


# In[318]:


data_may_new_MA_new.head()


# In[319]:


data_may_new_MA_new = pd.DataFrame(data_march_new_MA_new)


# In[320]:


data_may_new_MA_new.head()


# In[321]:


data_may_new_MA_new = data_may_new_MA_new.reset_index()


# In[322]:


data_may_new_MA_new.head()


# In[323]:


top_data_may_new_MA_new = data_may_new_MA_new.sort_values(by=['deaths'], 
                                                      ascending = False)


# In[324]:


top_data_may_new_MA_new.head()


# In[325]:


plt.figure(figsize=(15,6))
sns.barplot(x = 'county_name' , y = 'deaths', data = top_data_may_new_MA_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[326]:


plt.figure(figsize=(15,6))
sns.lineplot(x = 'county_name' , y = 'deaths', data = top_data_may_new_MA_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[327]:


plt.figure(figsize=(15,6))
sns.histplot(x = 'county_name' , y = 'deaths', data = top_data_may_new_MA_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[328]:


plt.figure(figsize=(15,6))
sns.scatterplot(x = 'county_name' , y = 'deaths', data = top_data_may_new_MA_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[329]:


# top 3 deaths in MA state County are: 
# 1. Middlesex County
# 2. Essex County 
# 3. Suffolk County


# In[330]:


data_june_new_MA= data_june_new[data_june_new['state_name'] == 'MA']


# In[331]:


data_june_new_MA.head()


# In[332]:


data_june_new_MA_new = data_june_new_MA[['county_name', 'deaths']]


# In[333]:


data_june_new_MA_new.head()


# In[334]:


data_june_new_MA_new.shape


# In[335]:


data_june_new_MA_new['deaths'].sum()


# In[336]:


data_june_new_MA_new.to_csv('data_june_new_MA_new.csv')


# In[337]:


data_june_new_MA_new = data_june_new_MA_new.groupby('county_name')['deaths'].sum()


# In[338]:


data_june_new_MA_new.head()


# In[339]:


data_june_new_MA_new = pd.DataFrame(data_june_new_MA_new)


# In[340]:


data_june_new_MA_new.head()


# In[341]:


data_june_new_MA_new = data_june_new_MA_new.reset_index()


# In[342]:


data_june_new_MA_new.head()


# In[343]:


top_data_june_new_MA_new = data_june_new_MA_new.sort_values(by=['deaths'], 
                                                      ascending = False)


# In[344]:


top_data_june_new_MA_new.head()


# In[345]:


plt.figure(figsize=(15,6))
sns.barplot(x = 'county_name' , y = 'deaths', data = top_data_june_new_MA_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[346]:


plt.figure(figsize=(15,6))
sns.lineplot(x = 'county_name' , y = 'deaths', data = top_data_june_new_MA_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[347]:


plt.figure(figsize=(15,6))
sns.histplot(x = 'county_name' , y = 'deaths', data = top_data_june_new_MA_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[348]:


plt.figure(figsize=(15,6))
sns.scatterplot(x = 'county_name' , y = 'deaths', data = top_data_june_new_MA_new.head(10))
plt.xticks(rotation = 90)
plt.show()


# In[349]:


# top 3 deaths in MA state County are: 
# 1. Middlesex County
# 2. Essex County 
# 3. Suffolk County


# In[352]:


import requests
import sys
import getopt


# In[ ]:


def send_slack_message(message):
    payload = '{"text":"%s"}'% message
    response = requests.post('https://hooks.slack.com/services/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',
                            data = payload)
    print(response.text)
def main(argv):
    message = ''
    try: opts, args = getopt.getopt(argv, 'hm:', ['message='])
    except getopt.GetoptError:
        print('SlackMessage.py -m <message>')
        sys.exit(2)
    if len(opts) == 0:
        message = "Covid Alerts !!!"
    for opt, arg in opts:
        if opt == '-h':
            print('SlackMessage.py -m <message>')
            sys.exit()
        elif opt in ('-m', '--message'):
            message = arg
    send_slack_message(message)
if __name__ ==  '__main__':
    main(sys.argv[1:])

