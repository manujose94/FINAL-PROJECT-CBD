#!/usr/bin/env python3
import matplotlib.pyplot as plt
  
users = []
reviews = []

topusers = []
topreviews = []

f = open('./4-task/part-00000','r')
mTotalReviews=0;
for row in f:
    row = row.split('\t')
    mTotalReviews+=int(row[1]);
    users.append(row[0])
    reviews.append(int(row[1]))


#Order by totalReviews  
index = list(range(len(reviews)))
index.sort(key = reviews.__getitem__)

users[:] = [users[i] for i in index]
reviews[:] = [reviews[i] for i in index]
reviews.reverse()
users.reverse()

percentOther=0
for idx, val in enumerate(reviews):
    if idx > 15:
        percentOther=100-sum(topreviews)
        break 
    topusers.append(users[idx])
    topreviews.append((val/mTotalReviews)*100)
    
   
colors = ['yellow', 'lightblue', '#2fce69','#bdecb6','cyan','#96c8a2','lightgreen','orange','#cc7000','darkorange', '#cb3234','red','#ff0080','#e79d9e',] 
fig, ax = plt.subplots(figsize=(16, 10))    
plt.title("TOP 15 REVIEWERS ({0}{1} of total)".format(sum(topreviews),"%"), fontsize = 12, y=1.08)
# plotting pie chart 
plt.pie(topreviews, labels = topusers, colors = colors, startangle = 90,
        shadow = True, radius = 1.2, autopct = '%1.1f%%') 
plt.show()