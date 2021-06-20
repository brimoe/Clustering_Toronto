#!/usr/bin/env python
# coding: utf-8

# #### Importing Libraries

# In[1]:


import requests 
from bs4 import BeautifulSoup
import pandas as pd 
import numpy as np 
import random 

get_ipython().system('pip install geopy')
from geopy.geocoders import Nominatim 
from pandas.io.json import json_normalize

get_ipython().system(' pip install folium==0.5.0')
import folium 

print('Folium installed')
print('Libraries imported.')


# #### Loading and Transforming Data

# In[2]:


req = requests.get("https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M")


# In[3]:


soup = BeautifulSoup(req.content, 'lxml')


# In[4]:


table = soup.find_all('table')[0]


# In[5]:


df = pd.read_html(str(table))


# In[6]:


neighbourhood = pd.DataFrame(df[0])


# In[7]:


neighbourhood.head(12)


# #### Cleaning Data

# In[8]:


neighbourhood = neighbourhood[neighbourhood != 'Not assigned']


# In[9]:


neighbourhood = neighbourhood.dropna()


# In[10]:


neighbourhood.reset_index(drop=True)


# In[11]:


neighbourhood = neighbourhood.reset_index(drop=True)
neighbourhood


# In[12]:


neighbourhood.shape


# #### Adding Latitude and Longitude to dataframe

# In[13]:


geo_data = pd.read_csv('https://cocl.us/Geospatial_data')
geo_data.head()


# In[14]:


geo_nd = neighbourhood.merge(geo_data, on = 'Postal Code', how = 'left')
geo_nd.head(12)


# In[15]:


toronto_df = geo_nd[geo_nd['Borough'].astype(str).str.contains('Toronto')]


# #### Generating folim map to visualize neighborhoods

# In[16]:


address = 'Toronto, Canada'

geolocator = Nominatim(user_agent="ca_explorer")
location = geolocator.geocode(address)
latitude = location.latitude
longitude = location.longitude
print('The geograpical coordinate of Canada are {}, {}.'.format(latitude, longitude))


# #### Clustered Neighborhood Map

# In[20]:


# create map of Toronto using latitude and longitude values
map_toronto = folium.Map(location=[latitude,longitude], zoom_start=14)

# adding markers to the map
for lat, lng, borough, neighborhood in zip(toronto_df['Latitude'], toronto_df['Longitude'],toronto_df['Neighbourhood'], toronto_df['Borough']):
    label = '{}, {}'.format(neighborhood, borough)
    label = folium.Popup(label, parse_html=True)
    folium.CircleMarker(
        [lat, lng],
        radius=5,
        popup=label,
        color='blue',
        fill=True,
        fill_color='#3186cc',
        fill_opacity=0.7,
        parse_html=False).add_to(map_toronto)  
    
map_toronto


# If unable to view map on Githib, please copy and paste the link into the search bar on the website: https://nbviewer.jupyter.org/

# In[ ]:




