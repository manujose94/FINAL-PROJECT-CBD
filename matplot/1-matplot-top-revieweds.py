#!/usr/bin/env python3
import matplotlib.pyplot as plt
  
names = []
marks = []

topnames = []
topmarks = []

ordernames = []
ordermarks = []  
f = open('./1-task/part-00000','r')
mTotalReviews=0;
for row in f:
    row = row.split('\t')
    mTotalReviews+=int(row[1]);
    if int(row[1]) > 550:
        names.append(row[0])
        marks.append(int(row[1]))

#Order by totalReviews  
index = list(range(len(marks)))
index.sort(key = marks.__getitem__)

ordernames[:] = [names[i] for i in index]
ordermarks[:] = [marks[i] for i in index]
ordermarks.reverse()
ordernames.reverse()
percentOther=0
for idx, val in enumerate(ordermarks):
    if idx > 15:
        print(mTotalReviews)
        print(sum(topmarks))
        percentOther=100-sum(topmarks)
        break 
    topnames.append(ordernames[idx])
    topmarks.append((val/mTotalReviews)*100)
    
   
colors = ['yellow', 'lightblue', 'green', 'cyan','red','lightgreen','orange','#cc7000','darkorange', 'darkred'] 
fig, ax = plt.subplots(figsize=(16, 10))    
plt.title("TOP 15 REVIEWD VIDEOGAMES ({0}{1} of total)".format(sum(topmarks),"%"), fontsize = 12, y=1.08)
# plotting pie chart 
plt.pie(topmarks, labels = topnames, colors = colors, startangle = 90,
        shadow = True, radius = 1.2, autopct = '%1.1f%%') 

plt.xticks(rotation=85,fontsize = 6)
plt.show()