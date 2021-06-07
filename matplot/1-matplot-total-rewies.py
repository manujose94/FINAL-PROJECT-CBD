#!/usr/bin/env python3
import matplotlib.pyplot as plt
  
names = []
marks = []

f = open('./1-task/part-00000','r')
mTotalReviews=0;
for row in f:
    row = row.split('\t')
    mTotalReviews+=int(row[1]);
    if int(row[1]) > 550:
        names.append(row[0])
        marks.append(int(row[1]))

fig, ax = plt.subplots(figsize=(20, 15))

# Define x and y axes
ax.bar(names, 
        marks,
        color = 'darkblue', 
       alpha = 0.3)

# Set plot title and axes labels
ax.set(title = "Reviews by Game Amazon (more than 550)")
plt.ylabel('Number of Reviews', fontsize=12)
plt.subplots_adjust(top=0.97, bottom=0.307, left=0.09, right=0.94)
plt.xticks(rotation=85,fontsize =11)
plt.show()