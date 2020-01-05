from csv import reader

#function container#

#function that allows us to explore the data of a determined set of apps
def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]    
    for row in dataset_slice:
        print(row)
        print('\n') # adds a new (empty) line between rows
        
    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))

#function that checks if a string is in english by checking if less than 3 characters are ASCII
def is_english(string):
    non_ascii = 0
    
    for character in string:
        if ord(character) > 127:
            non_ascii += 1
    
    if non_ascii > 3:
        return False
    else:
        return True

#creating a frequency table of the apps with percentages
def freq_table(dataset, index):
    table = {}
    total = 0
    
    for row in dataset:
        total += 1
        value = row[index]
        if value in table:
            table[value] += 1
        else:
            table[value] = 1
    
    table_percentages = {}
    for key in table:
        percentage = (table[key] / total) * 100
        table_percentages[key] = percentage 
    
    return table_percentages

#print display table that 
def display_table(dataset, index):
    table = freq_table(dataset, index)
    table_display = []
    for key in table:
        key_val_as_tuple = (table[key], key)
        table_display.append(key_val_as_tuple)
        
    table_sorted = sorted(table_display, reverse = True)
    for entry in table_sorted:
        print(entry[1], ':', entry[0])


### The Google Play data set ###
opened_file = open('googleplaystore.csv')
read_file = reader(opened_file)
android = list(read_file)
android_header = android[0]
android = android[1:]

### The App Store data set ###
opened_file = open('AppleStore.csv')
read_file = reader(opened_file)
ios = list(read_file)
ios_header = ios[0]
ios = ios[1:]


# print(android_header)
# print('\n')
# explore_data(android, 0, 3, True)

# print(ios_header)
# print('\n')
# explore_data(ios, 0, 3, True)

# print(android[10472])  # incorrect row
# print('\n')
# print(android_header)  # header
# print('\n')
# print(android[0])      # correct row

# print(len(android))
# #del android[10472]  # don't run this more than once
# print(len(android))

# for app in android:
#     name = app[0]
#     if name == 'Instagram':
#         print(app)

#cleaning up and removing duplicate apps from the list 
duplicate_apps = []
unique_apps = []

for app in android:
    name = app[0]
    if name in unique_apps:
        duplicate_apps.append(name)
    else:
        unique_apps.append(name)
    
# print('Number of duplicate apps:', len(duplicate_apps))
# print('\n')
# print('Examples of duplicate apps:', duplicate_apps[:15])


#finding the max reviews in the list
reviews_max = {}

for app in android:
    name = app[0]
    n_reviews = float(app[2])
    
    if name in reviews_max and reviews_max[name] < n_reviews:
        reviews_max[name] = n_reviews
        
    elif name not in reviews_max:
        reviews_max[name] = n_reviews

# #validating if the length of the list is correct
# print('Expected length:', len(android) - 1181)
# print('Actual length:', len(reviews_max))


android_clean = []
already_added = []

for app in android:
    name = app[0]
    n_reviews = float(app[2])
    
    if (reviews_max[name] == n_reviews) and (name not in already_added):
        android_clean.append(app)
        already_added.append(name) # make sure this is inside the if block

explore_data(android_clean, 0, 3, True)

# print(ios[813][1])
# print(ios[6731][1])

# print(android_clean[4412][0])
# print(android_clean[7940][0])

# print(is_english('Docs To Go™ Free Office Suite'))
# print(is_english('Instachat 😜'))
# print(ord('™'))
# print(ord('😜'))


#stores english apps in a seperate struct for both andrioid and ios
android_english = []
ios_english = []

for app in android_clean:
    name = app[0]
    if is_english(name):
        android_english.append(app)
        
for app in ios:
    name = app[1]
    if is_english(name):
        ios_english.append(app)
        
# explore_data(android_english, 0, 3, True)
# print('\n')
# explore_data(ios_english, 0, 3, True)

android_final = []
ios_final = []

for app in android_english:
    price = app[7]
    if price == '0':
        android_final.append(app)
        
for app in ios_english:
    price = app[4]
    if price == '0.0':
        ios_final.append(app)
        
# print(len(android_final))
# print(len(ios_final))

# display_table(ios_final, -5)
# display_table(android_final, 1) # Category
# display_table(android_final, -4)

genres_ios = freq_table(ios_final, -5)

#check avg ratings for each genre ios
for genre in genres_ios:
    total = 0
    len_genre = 0
    for app in ios_final:
        genre_app = app[-5]
        if genre_app == genre:            
            n_ratings = float(app[5])
            total += n_ratings
            len_genre += 1
    avg_n_ratings = total / len_genre
    print(genre, ':', avg_n_ratings)

# #print navigation apps
# for app in ios_final:
# 	if app[-5] == 'Navigation':
# 		print(app[1], ":", app[5]) #print name and numbder of ratings

# #print refrence apps
# for app in ios_final:
# 	if app[-5] == 'Refrence':
# 		print(app[1], ':', app[5])

