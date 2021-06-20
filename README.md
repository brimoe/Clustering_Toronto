# Segmenting and Clustering Neighborhoods in Toronto
### IBM Applied Data Science Capstone: Case Study Project 

Date: Feb 2021

### Introduction:
For this data project, I segmented and clustered the neighborhoods in Toronto, Canada, based on postal code and district information found from an open data source. Then, I generated a folium map to visualize the communities and how they cluster together.

### Data : 
The data I used is a Wikipedia page with the postal code and district information for [Toronto](https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M). Considering the latitude and longitude values were not included in the data, I used a separate [CSV_file](https://cocl.us/Geospatial_data) that contains the geographical coordinates of each postal code. 

### Methodology: 
To prepare for this analysis, I used the beautiful soup package to scrape the Wikipedia page, wrangle, clean, then transform the data into a pandas data frame. After converting the data for each neighborhood into a data frame, I added the geospatial CSV file into my data frame. Finally, I utilized the Foursquare location data to get the geographical coordinates of Toronto, Canada and displayed my data in a folium map. 

