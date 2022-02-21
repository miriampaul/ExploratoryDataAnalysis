#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd


# In[6]:


import numpy as np


# In[7]:


import folium


# # US Accidents Exploratory Data Analysis

# #Source- Kaggle

# #Information about accidents

# ##can use useful to prevent accidents           
# 
# 
# 
# ##mention that this does not contain data about NewYork

# In[8]:


pip install opendatasets --upgrade --quiet


# Download the data

# In[9]:


import opendatasets as od
download_url='https://www.kaggle.com/sobhanmoosavi/us-accidents'
od.download(download_url)


# # Prepare data for cleaning

# In[10]:


dataset=pd.read_csv(r'C:\Users\miria\OneDrive\GoogleDataAnalytics\Project\US_Accidents_Dec20_updated.csv')

dataset.head()
# In[11]:


dataset.head()


# In[12]:


dataset.columns


# In[13]:


len(dataset.columns) #Number of columns


# In[14]:


dataset.info()


# In[15]:


dataset.describe()


# In[16]:


numerics=['int16','int32,' ' int64', 'float16', 'float32','float64']
numeric_df=dataset.select_dtypes(include=numerics)
len(numeric_df.columns)


# # Count Number of missing values

# In[17]:


dataset.isna().sum()


# Percentage of Missing values per column
# 

# In[18]:


missing_percentages=dataset.isna().sum().sort_values(ascending=False)/len(dataset)
missing_percentages


# In[19]:


missing_percentages[missing_percentages != 0] #gives columns which has missing values


# In[20]:


type(missing_percentages)


# In[21]:


missing_percentages[missing_percentages != 0].plot(kind='barh')


# Remove columns that you don't want to use

# In[ ]:





# In[22]:


dataset.columns


# # Exploratory Analysis and visualization
# Columns we will analyze:
# 1. City
# 2.Start_Lat
# 3.Start_Lng
# 4.Temperature
# 5.Weather Condition

# # City

# In[23]:


dataset.City


# In[24]:


cities=dataset.City.unique()
len(cities)


# In[25]:


cities[:100]


# In[26]:


cities_by_accident=dataset.City.value_counts()
cities_by_accident


# In[27]:


cities_by_accident[:20]#Count of first 20 cities


# In[28]:


'New York' in dataset.City


# In[29]:


'NY' in dataset.State


# In[30]:


cities_by_accident[:20].plot(kind='barh')


# In[31]:


import seaborn as sns


# In[32]:


sns.set_style('darkgrid') #to change theme to dark


# In[41]:


sns.distplot(cities_by_accident)


# In[42]:


high_accident_cities=cities_by_accident[cities_by_accident>=1000]
low_accident_cities=cities_by_accident[cities_by_accident<1000]


# In[43]:


len(high_accident_cities)


# In[44]:


len(low_accident_cities)


# In[45]:


sns.distplot(high_accident_cities)


# In[46]:


sns.displot(low_accident_cities)


# In[47]:


sns.histplot(cities_by_accident,log_scale=True)


# In[48]:


cities_by_accident[cities_by_accident==1]


# In[ ]:





# # Start_Time

# In[49]:


dataset.Start_Time[0]


# In[50]:


dataset.Start_Time =pd.to_datetime(dataset.Start_Time)


# In[51]:


dataset.Start_Time[0].hour


# In[52]:


dataset.Start_Time.dt.hour


# In[53]:


sns.histplot(dataset.Start_Time.dt.hour,bins=24)


# In[54]:


sns.distplot(dataset.Start_Time.dt.hour, bins=24, kde=False, norm_hist=True)


# # - A high percentage of accidents occur between 4pm-7PM and  6am to 10AM 
# 

# In[55]:


sns.distplot(dataset.Start_Time.dt.dayofweek, bins=24, kde=False, norm_hist=True)


# Is the distribution of accidents by hour the same on weekends as on weekdays.

# In[56]:


dataset.Start_Time[dataset.Start_Time.dt.dayofweek==6]


# In[57]:


sundays_Start_Time=dataset.Start_Time[dataset.Start_Time.dt.dayofweek==6]


# In[58]:


sns.displot(sundays_Start_Time.dt.hour, bins=24, kde=False, norm_hist=True)


# In[ ]:


df_2019=dataset[dataset.Start_Time.dt.year=='2019']


# In[ ]:


df_2019


# In[ ]:


dataset.Start_Time


# In[ ]:


Year_2019=dataset.Start_Time[dataset.Start_Time==2019]


# In[ ]:


Year_2019


# In[ ]:


sns.distplot(df_2019.Start_Time.dt.month, bins=24, kde=False, norm_hist=True)


# In[59]:


dataset.columns


# In[60]:


dataset.Station.value_counts().plot(kind='pie')


# # Start_Lat and Start_Lng

# In[61]:


dataset.Start_Lat


# In[62]:


dataset.Start_Lng


# In[63]:


sns.scatterplot(x=dataset.Start_Lng, y=dataset.Start_Lat, size=0.001)


# In[64]:


sample_df=dataset.sample(int(0.1 * len(dataset)))


# In[65]:


import folium


# In[66]:


lat, lon =dataset.Start_Lat[0],dataset.Start_Lng[0]


# In[67]:


lat, lon


# In[72]:


for x in dataset[['Start_Lat','Start_Lng']].sample(100).iteritems():
    print(x)


# In[71]:


map=folium.Map()
for lat, lon in 
marker=folium.Marker((lat,lon))
marker.add_to(map)


# In[85]:


sample_df=dataset.sample(int(0.1*len(dataset)))
lat_lon_pairs=list(zip(list(sample_df.Start_Lat), list(sample_df.Start_Lng)))


# In[86]:


from folium.plugins import HeatMap


# In[87]:


map = folium.Map()
HeatMap(lat_lon_pairs).add_to(map)
map


# In[77]:


zip (list(dataset.Start_Lat), list(dataset.Start_Lng))


# In[ ]:





# In[56]:


#Ask and Answer questions


# 1. Are there more accidents in warmer or colder area
# 2. Which states have the highest number of accidents?
# 3. How about per capita?
# 4. Does New York Show up in the data? if yes why is the count lower in this most populated cites?
# 5.Among the top 100 cities in number which states do they belong to most frequently?
# 6.What time of the day are accidents most frequent in?
# 7.Which months have the most accidents?
# 8.What is the trend of accidents year over year? (increasing/decreasing)?
# 9.When is accidents per unit of traffic higher?
# 
# 

# In[ ]:





# In[ ]:



#Summary and conculsion


# 1. No data for NewYork

# 2.Less than 251 cities have more than 1000 accidents

# 3.Over 1100 cities have reported just one accident 

# The number of accident per city decreases exponentially

# In[ ]:




