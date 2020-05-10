import matplotlib as plt

#to generate plot on backend - needed to update any changes made to a plot before showing
plt.plot()
#to show plot
plt.show()

#pick first twelve rows
first_twelve = unrate[0:12]
#graph date on x and value on y
plt.plot(first_twelve['DATE'], first_twelve['VALUE'])
plt.show()

#rotate the graph xticks by 90 degrees
plt.plot(first_twelve['DATE'], first_twelve['VALUE'])
plt.xticks(rotation=90)
plt.show()

#add labels to axis and title
plt.plot(first_twelve['DATE'], first_twelve['VALUE'])
plt.xticks(rotation=90)
plt.xlabel('Month')
plt.ylabel('Unemployment Rate')
plt.title('Monthly Unemployment Trends, 1948')
plt.show()

#plot rate in the first 12 listed months
import pandas as pd
import matplotlib.pyplot as plt

unrate = pd.read_csv('unrate.csv')
unrate['DATE'] = pd.to_datetime(unrate['DATE'])
first_twelve = unrate[0:12]

plt.plot(first_twelve['DATE'], first_twelve['VALUE'])
plt.xticks(rotation=90)
plt.xlabel('Month')
plt.ylabel('Unemployment Rate')
plt.title('Monthly Unemployment Trends, 1948')
plt.show()


#create subplots
import matplotlib.pyplot as plt

fig = plt.figure()

ax1 = fig.add_subplot(2,1,1)
# (vertical count of plots, horizontal count of plots, plot index)
ax2 = fig.add_subplot(2,1,2)
plt.show()

#creating subplots with diffrent scales
import matplotlib.pyplot as plt

fig = plt.figure()
#same but this sets plot size to 12 inches width by 5 inches height 
fig = plt.figure(figsize=(12, 5))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

ax1.plot(unrate[0:12]['DATE'], unrate[0:12]['VALUE'])
ax2.plot(unrate[12:24]['DATE'], unrate[12:24]['VALUE'])

plt.show()


#divide it up into five plots with one plot for each year
#set plot size to 12 height and 12 width
fig = plt.figure(figsize=(12,12))
#generate a grid of 5 rows and 1 column and plot individual years data
for i in range(5):
    ax = fig.add_subplot(5,1,i+1)
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    ax.plot(subset['DATE'], subset['VALUE'])
#show using plt
plt.show()


#plot two lines on the same graph with diffrent colors
unrate['MONTH'] = unrate['DATE'].dt.month
fig = plt.figure(figsize=(6,3))

plt.plot(unrate[0:12]['MONTH'], unrate[0:12]['VALUE'], c='red')
plt.plot(unrate[0:12]['MONTH'], unrate[12:24]['VALUE'], c='blue')

plt.show()

#breaking up plots by colors
fig = plt.figure(figsize=(10,6))
colors = ['red', 'blue', 'green', 'orange', 'black']
for i in range(5):
    start_index = i*12
    end_index = (i+1)*12
    subset = unrate[start_index:end_index]
    plt.plot(subset['MONTH'], subset['VALUE'], c=colors[i])
plt.show()