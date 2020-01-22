from __future__ import print_function
import pandas as pd

#pandas has two main data structures that are implemented in classes:
#the DataFrame, which you can imagine as a relational data table, with rows and named columns.
#the Series, which is a single column. A DataFrame contains one or more Series and a name for each Series.

#two examples of series
city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])

#example of dataframe linking the two series above
pd.DataFrame({ 'City name': city_names, 'Population': population })
