#how to clean columns of a list that include paranthesis
for item in moma:
    nationality = item[2]
    nationality = nationality.replace('(', '')
    nationality = nationality.replace(')', '')
    item[2] = nationality
    
    gender = item[5]
    gender = gender.replace('(', '')
    gender = gender.replace(')', '')
    item[5] = gender

#clean unkowns
for row in moma:
    gender = row[5]
    gender = gender.title()
    if not gender:
        gender = "Gender Unknown/Other"
    row[5] = gender

    nationality = row[2]
    nationality = nationality.title()
    if not nationality:
        nationality = "Nationality Unknown"
    row[2] = nationality


#clean dates
test_data = ["1912", "1929", "1913-1923",
             "(1951)", "1994", "1934",
             "c. 1915", "1995", "c. 1912",
             "(1988)", "2002", "1957-1959",
             "c. 1955.", "c. 1970's", 
             "C. 1990-1999"]

bad_chars = ["(",")","c","C",".","s","'", " "]

processed_test_data = []

def strip_characters(string):
    for char in bad_chars:
        string = string.replace(char,"")
    return string

def process_date(string):
    result = ""
    if '-' in string:
        year1,year2 = string.split('-', 1)
        sum_year = float(year1) + float(year2)
        average = sum_year/2
        average = round(average)
        result = int(average)
    else:
        result = int(string)
        
    return result

stripped_test_data = ['1912', '1929', '1913-1923',
                      '1951', '1994', '1934',
                      '1915', '1995', '1912',
                      '1988', '2002', '1957-1959',
                      '1955', '1970', '1990-1999']

for date in stripped_test_data:
    result = process_date(date)
    processed_test_data.append(result)
    

for item in moma:
    date = item[6]
    date = strip_characters(date)
    date = process_date(date)
    item[6] = date

#Extract the manufacturer name from the cpu column. Assign it to a new column cpu_manufacturer
laptops["gpu_manufacturer"] = (laptops["gpu"]
                                       .str.split()
                                       .str[0]
                              )
#Use the Series.value_counts() method to find the counts of each manufacturer in cpu_manufacturer. Assign the result to cpu_manufacturer_counts
laptops["cpu_manufacturer"] = (laptops["cpu"]
                                       .str.split()
                                       .str[0]
                              )
cpu_manufacturer_counts = laptops["cpu_manufacturer"].value_counts()

#replace incorrect and mispilled OS values
mapping_dict = {
    'Android': 'Android',
    'Chrome OS': 'Chrome OS',
    'Linux': 'Linux',
    'Mac OS': 'macOS',
    'No OS': 'No OS',
    'Windows': 'Windows',
    'macOS': 'macOS'
}

laptops["os"] = laptops["os"].map(mapping_dict)