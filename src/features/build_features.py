#%%
# imports
import pandas as pd
#%%
# One liner to find a list of datetimes, incremented by month, between two dates.
import datetime
from dateutil.rrule import rrule, MONTHLY

strt_dt = datetime.date(2001,1,1)
end_dt = datetime.date(2005,6,1)

dates = [dt for dt in rrule(MONTHLY, dtstart=strt_dt, until=end_dt)]
#%%
# Create a label (category) encoder object
le = preprocessing.LabelEncoder()
#%%
# Fit the encoder to the pandas column
le.fit(df['property_type'])
#%%
# View the labels (if you want)
list(le.classes_)
#%%
# Apply the fitted encoder to the pandas column
df['property_type_transform'] = le.transform(df['property_type'])
#%%
df
#%%
# Convert some integers into their category names
# list(le.inverse_transform([2, 2, 1]))
#%%
df[(df['property_type'] == "F") | (df['property_type'] == "T")]
#%%
df.postcode.unique()
#%%
# return a single row
df[(df['property_type'] == "F") & (df['postcode'] == "E1 0AE")]
df.iloc[[3]]
#%%
df[(df['property_type'] == "T") & (df['postcode'] == "WC2R 3JJ")]