#%%
# import dependencies
from sklearn import preprocessing
from pygeocoder import Geocoder
import pandas as pd
import requests
import json
#%% 
# import data
pricing_data = pd.read_csv('../data-science/summative-assignment/data/raw/01_06_2014_until_04_06_2019.csv')
postcode_data = pd.read_csv('../data-science/summative-assignment/data/raw/NSPL_MAY_2019_UK.csv', low_memory=False)


#%%
# import the latlong csv
latlong = pd.read_csv('../data-science/summative-assignment/merged_latlon.csv')
#%%
latlong.dtypes
#%% Combine the lat and the long into 1 feature
latlong['property_type']
#%%
# import the data to analyse
df = pd.read_csv('../data-science/summative-assignment/01_06_2014_until_04_06_2019.csv')
#%%
df.isna().sum()
#%%
# Geocoding
# get an array of unique postcodes... of which there are 66612
postcodes = df.postcode.unique()
# postcodes.loc[:, 'areacode']
postcodes = pd.DataFrame(postcodes, columns=['postcode'])
postcodes
#%%
# Merge
left = pd.read_csv('../data-science/summative-assignment/01_06_2014_until_04_06_2019.csv')
right = df
merged = pd.merge(left, right, how='inner', left_on='postcode', right_on='pcd')
#%%
filename = '../data-science/summative-assignment/merged.csv'
merged.to_csv(filename, encoding='utf-8', index=False)
#%%
merged.isna().sum()
#%%
df
#%%
postcodes['areacode'] = df.postcode.str[:1]
postcodes
# postcodes['']

# Solution 1 - API Call
# check for NaN in python list
# for each 100 items
# call the api
# parse the response
# map the response

# Solution 2 - CSV Lookup

# load df with postcodes
# batch by area code
# groupby areacode
# open respective csv file ('NSPL_MAY_2019_UK_{}.csv').format(areacode)
# choose columns wanted, lookup and append to respective row in df
#%% [markdown]
# Solution 3 - Joining Tables
# postcode lookup (2628568, 41)
# our addresses (345551, 16)
# our merged (157472, 57)
# this means that 188,079 addresses were actually duplicates?
#%%
# We can load the 1gb master csv of postcode data into memory with pandas
right = pd.read_csv('../data-science/summative-assignment/data/NSPL_MAY_2019_UK.csv', low_memory=False)
right.shape
#%%
# Then load our csv with addresses into a dataframe (tables)
left = pd.read_csv('../data-science/summative-assignment/01_06_2014_until_04_06_2019.csv')
left.shape
#%% 
# Using the merge function to join the two dataframes
merged = pd.merge(left, right, how='inner', left_on='postcode', right_on='pcd')
#%%
merged.shape
#%%
filename = '../data-science/summative-assignment/merged_latlon.csv'
merged.to_csv(filename, encoding='utf-8', index=False)
#%%
body = json.dumps(postcodes)
body
#%%
# then use the postcode api to bulk lookup our latlongs
url = 'https://api.postcodes.io/postcodes'
r = requests.post(url, json=body)
data_as_text = r.text
data_as_json = r.json()
#%%
data_as_text
#%%
with open('postcode_data.json', 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, ensure_ascii=False, indent=2)
#%%
# Look at the datatypes
df.dtypes
#%%
# Return the unique values in each column of the dataset.
for col in df:
    print('Column %s is of type %s and unique values are as follows' % (df[col].name, df[col].dtype))
    print(df[col].unique())
#%%
df.shape
#%% [markdown]
# ## Check for null values
#%%
df.isnull().values.any()
#%%
# Drop variables we're not interested in
df.drop(['unique_id', 'paon', 'saon', 'linked_data_url', ], axis=1)
#%%
df['postcode'].replace({'\'': '"'}, regex=True)
#%%
df

#%%
# For geocoding, we need to submit a string containing an address or location (such as a city) into the geocode function. However, not all strings are formatted in a way that Google’s geo-API can make sense of them. We can text if an input is valid by using the .geocode().valid_address function.
# Verify that an address is valid (i.e. in Google's system)
Geocoder.geocode("4207 N Washington Ave, Douglas, AZ 85607").valid_address
#%% [markdown]
# Because the output was True, we now know that this is a valid address and thus can print the latitude and longitude coordinates.
#%%
# Print the lat/long
results.coordinates
# But even more interesting, once the address is processed by the Google geo API, we can parse it and easily separate street numbers, street names, etc.
#%%
# Find the lat/long of a certain address
result = Geocoder.geocode("7250 South Tucson Boulevard, Tucson, AZ 85756")
#%%
# Print the street number
result.street_number
#%%
# Print the street name
result.route
#%%
df.property_type.unique()

