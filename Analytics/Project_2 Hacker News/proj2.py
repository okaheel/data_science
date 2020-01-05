import csv
import datetime as dt

opened_file = open("hacker_news.csv")
read_file = csv.reader(opened_file)
hn = list(read_file)

#print(hn[:5])

#remove headers from list

headers = hn[0]
hn = hn[1:]

#check cleaning
# print(headers)
# print(hn[:5])

ask_posts = []
show_posts = []
other_posts = []

#place ask and show posts into sepearate lists
for post in hn:
	title = post[1]
	if title.lower().startswith("ask hn"):
		ask_posts.append(post)
	elif title.lower().startswith("show hn"):
		show_posts.append(post)
	else:
		other_posts.append(post)

print(len(ask_posts))
print(len(show_posts))
print(len(other_posts))

#count comments in ask posts
total_ask_comments = 0

for post in ask_posts:
	total_ask_comments += int(post[4])

#find the average number of comments per post
avg_ask_comments = total_ask_comments/ len(ask_posts)
print(avg_ask_comments)

#count the total number of comments per show post
total_show_comments = 0

for post in show_posts:
	total_show_comments += int(post[4])

#find the average number of comments per show post
avg_show_comments = total_show_comments / len(show_posts)
print(avg_show_comments)

result_list = []

#create a list of posts with creation times and the comments
for post in ask_posts:
	created_time = post[6]
	n_comments = int(post[4])
	result_list.append([created_time, n_comments])

counts_by_hour = {}
comments_by_hour = {}
date_format = "%m/%d/%Y %H:%M"

#create a list of the number of comments per hour
for row in result_list:
    date = row[0]
    comment = row[1]
    time = dt.datetime.strptime(date, date_format).strftime("%H")
    if time in counts_by_hour:
        comments_by_hour[time] += comment
        counts_by_hour[time] += 1
    else:
        comments_by_hour[time] = comment
        counts_by_hour[time] = 1

print(comments_by_hour)
print('\n')
print(counts_by_hour)

#create a list and caluclate the avg number of comments per hour
avg_by_hour = []

#calculate the number of comments per hour
for hr in comments_by_hour:
	avg_by_hour.append([hr, comments_by_hour[hr]/ counts_by_hour[hr]])

avg_by_hour

#create a list to order in reverse order by frequency
swap_avg_by_hour = []

for row in avg_by_hour:
	swap_avg_by_hour.append([row[1], row[0]])

print(swap_avg_by_hour)

sorted_swap = sorted(swap_avg_by_hour, reverse = True)

sorted_swap

#print the top 5 hours for comments
print("Top 5 Hours for 'Ask HN' Comments")
for avg, hr in sorted_swap[:5]:
	print(
        "{}: {:.2f} average comments per post".format(
            dt.datetime.strptime(hr, "%H").strftime("%H:%M"),avg
        )
    )
