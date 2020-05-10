import pandas as pd
import numpy as np

auto = pd.read_csv("autos.csv", index_col = 0, encoding ='Latin-1')

#inspect df
#print(auto)

auto_info = auto.info()
auto_head = auto.head()
auto_columns = auto.columns

auto.columns = ['name', 'seller', 'offer_type', 'price', 'ab_test', 'vehicle_type', 'registration_year', 'gearbox', 'power_ps', 'model', 'odometer', 'registration_month', 'fuel_type', 'brand', 'unrepaired_damage', 'ad_created', 'num_photos', 'postal_code', 'last_seen']

auto = auto.drop(["num_photos", "seller", "offer_type"], axis=1)

auto["price"] = (auto["price"]
                        .str.replace("$","")
                        .str.replace(",","")
                        .astype(int)
                        )
                        
print(auto["price"].head())
