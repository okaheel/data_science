import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

# save filepath to variable for easier access
melbourne_file_path = 'melb_data.csv'
# read the data and store data in DataFrame titled melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path) 

#filer rows with missing price value
filtered_melbourne_data = melbourne_data.dropna(axis=0)

#choose target
y = filtered_melbourne_data.Price

#choose features
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude']

#choose input struct 
X = filtered_melbourne_data[melbourne_features]

#define model
melbourne_model = DecisionTreeRegressor()
#fit model
melbourne_model.fit(X, y)

#create predictions
predicted_home_prices = melbourne_model.predict(X)
#calculate MAE
MAE = mean_absolute_error(y, predicted_home_prices)
print(MAE)
#in sample error was approx $500

#split data into training and validation data
#split is based on random number generator

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)
melbourne_model = DecisionTreeRegressor()
#fit model
melbourne_model.fit(train_X, train_y)

#get predicted prices on validation data
val_predictions = melbourne_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))
#error on out of sample is approx $260k