#!/usr/bin/env python3
import matplotlib.pyplot as plt
import pandas as pd  
items = []
reviews = []

starts_1,starts_2,starts_3,starts_4 ,starts_5= ([] for i in range(5))
topstarts = []

f = open('./3-task/part-00000','r')
mTotalReviews=0;
for row in f:
    row = row.split('\t')
    mTotalReviews+=int(row[2]);
    if int(row[2]) > 800:
        items.append(row[0])
        reviews.append(int(row[2]))
        starts = row[3].split(':')
        starts_1.append(int(starts[0]))
        starts_2.append(int(starts[1]))
        starts_3.append(int(starts[2]))
        starts_4.append(int(starts[3]))
        starts_5.append(int(starts[4]))

plotdata = pd.DataFrame({
    "1 starts":starts_1,
    "2 starts":starts_2,
    "3 starts":starts_3,
    "4 starts":starts_4,
    "5 starts":starts_5
    }, index=items )

 
colors=['darkred','red','#cc7000','orange','#e6e600']
plotdata.plot(kind='bar', stacked=True,color=colors,figsize=(16, 10))
plt.subplots_adjust(top=0.98, bottom=0.265, left=0.09, right=0.94)
plt.title("Video games over 800 reviews")
plt.ylabel("Number of reviews",fontsize = 12)
plt.legend(fontsize='x-large', title_fontsize='40')
plt.xticks(rotation=85,fontsize = 9.5)
plt.show()