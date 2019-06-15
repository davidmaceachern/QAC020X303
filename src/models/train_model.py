#%%
from sklearn.linear_model import LinearRegression
# Split data into predictors X and output Y
predictors = ['lat', 'long']
X = latlong[predictors]
y = latlong['price_paid']
# Initialise and fit model
lm = LinearRegression()
model = lm.fit(X, y)
#%%
print(f'alpha = {model.intercept_}')
print(f'betas = {model.coef_}')