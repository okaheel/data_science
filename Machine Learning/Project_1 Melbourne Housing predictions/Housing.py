import pandas as pd
from sklearn.tree import DecisionTreeRegressor

# save filepath to variable for easier access
melbourne_file_path = 'melb_data.csv'
# read the data and store data in DataFrame titled melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path) 


# print a summary of the data in Melbourne data
#print(melbourne_data.columns)


# The Melbourne data has some missing values (some houses for which some variables weren't recorded.)
# We'll learn to handle missing values in a later tutorial.  
# Your Iowa data doesn't have missing values in the columns you use. 
# So we will take the simplest option for now, and drop houses from our data. 
# Don't worry about this much for now, though the code is:

# dropna drops missing values (think of na as "not available")
melbourne_data = melbourne_data.dropna(axis=0)

#dot notation to select column we want to predict and set as preciction target (y)
y = melbourne_data.Price

#selecting features that we want to use to make predictions
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']

#set training data to x
X = melbourne_data[melbourne_features]

#review data before training model
#print(X.describe())

#visually inspect the start of the table
#print(X.head())

#since data is stored in a data frame we will be using SKlearn to model
# Define model
#specify number of random states to ensure same results when running multiple runs

melbourne_model = DecisionTreeRegressor(random_state = 1)

#fit model
melbourne_model.fit(X, y)

#showing data bore predictions
print("Predictions for the following 5 houses")
print(X.head())

#make prediction

print("Price predictions are: ")
print(melbourne_model.predict(X.head()))
