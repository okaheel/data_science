#check the shape and type of a dataframe
import pandas as pd
f500 = pd.read_csv('f500.csv',index_col=0)
f500.index.name = None
f500_shape = f500.shape
f500_type = type(f500)

#check the head of the dataframe
f500_head = f500.head(6) #get the first 6 items
f500_tail = f500.tail(8) #get the last 8 items

#use the info method to check information about the dataframe
f500.info()

#
import pandas as pd
# read the data set into a pandas dataframe
f500 = pd.read_csv("f500.csv", index_col=0)
f500.index.name = None

# replace 0 values in the "previous_rank" column with NaN
f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan

f500_selection = f500[['rank', 'revenues', 'revenue_change']].head()

#companies that are in brazil or venezual
brazil_venezuela = f500[(f500["country"] == "Brazil") | (f500["country"] == "Venezuela")]

#top 5 tech comapines outside of the US
tech_outside_usa = f500[(f500["sector"] == "Technology") & (f500["country"] != "USA")].head(5)

#remove GB from the ram columns
#find the unique ram values that laptops have
laptops["ram"] = laptops["ram"].str.replace('GB','')
unique_ram = laptops["ram"].unique()

#use pandas to date time function to turn convert date into datetime values
unrate = pd.read_csv("unrate.csv")
unrate['DATE'] = pd.to_datetime(unrate['DATE'])
unrate.head(12)