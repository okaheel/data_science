#convert csv into np array
import csv
import numpy as np

# import nyc_taxi.csv as a list of lists
f = open("nyc_taxis.csv", "r")
taxi_list = list(csv.reader(f))

# remove the header row
taxi_list = taxi_list[1:]

converted_taxi_list = []
for row in taxi_list:
    converted_row = []
    for item in row:
        converted_row.append(float(item))
    converted_taxi_list.append(converted_row)

taxi = np.array(converted_taxi_list)

#boolean indexing  with np
#filtering through rides to find what rides were in jan and feb
pickup_month = taxi[:,1]

january_bool = (pickup_month == 1)
january = pickup_month[january_bool]
january_rides = january.shape[0]
print(january_rides)

february_bool = (pickup_month == 2)
february = pickup_month[february_bool]
february_rides = february.shape[0]
print(february_rides)

#check the shape and type of a dataframe
f500 = pd.read_csv('f500.csv',index_col=0)
f500_shape = f500.shape
f500_type = type(f500)

#remove columns with null values
laptops_no_null_rows = laptops.dropna(axis = 1)
#remove rows with null values
laptops_no_null_cols = laptops.dropna(axis = 0)