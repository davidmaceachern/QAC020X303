#%%
# import dependencies
from sklearn import preprocessing
from pygeocoder import Geocoder
import pandas as pd
import requests
import json
#%%
# -----------------------------------------
# MCAR


#%%
# -----------------------------------------
# Merge datasets
#%%
pricing_data = pd.read_csv('../data-science/summative-assignment/data/raw/01_06_2014_until_04_06_2019.csv')
# We can load the 1gb master csv of postcode data into memory with pandas
postcode_data = pd.read_csv('../data-science/summative-assignment/data/raw/NSPL_MAY_2019_UK.csv', low_memory=False)
#%%
# Merge
left = pd.read_csv('../data-science/summative-assignment/01_06_2014_until_04_06_2019.csv')
right = df
merged = pd.merge(left, right, how='inner', left_on='postcode', right_on='pcd')
#%%
filename = '../data-science/summative-assignment/data/interim/merged.csv'
merged.to_csv(filename, encoding='utf-8', index=False)
#%%
merged.shape
#%%
merged.isna().sum()
# -----------------------------------------
# Exploring the dataset
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
# Check for total number of null values
df.isna().sum()
# -----------------------------------------
# Using Google maps wrapper for geocoding
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
# -----------------------------------------
# Using an Api to lookup postcodes
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

# -----------------------------------------
# Misc
#%%
# split the string to try to get area code.
postcodes['areacode'] = df.postcode.str[:1]
#%%
# trying to convert previous array of postcodes for api call
# get an array of unique postcodes... of which there are 66612
postcodes = df.postcode.unique()
# postcodes.loc[:, 'areacode']
postcodes = pd.DataFrame(postcodes, columns=['postcode'])
postcodes
body = json.dumps(postcodes)
body