#!/usr/bin/env python3
import matplotlib.pyplot as plt
import pandas as pd  
import numpy as np
from matplotlib.ticker import StrMethodFormatter
items = []
reviews = []
topstarts = []

score=[];

orderitems = []
orderscore=[]
f = open('./3-task/part-00000','r')
mTotalReviews=0;
for row in f:
    row = row.split('\t')
    mTotalReviews+=int(row[2]);
    if int(row[2]) > 800:
        items.append(row[0])
        reviews.append(int(row[2]))
        score.append(float(row[1]))

#Order Arrays
index = list(range(len(score)))
index.sort(key = score.__getitem__)
items[:] = [items[i] for i in index]
score[:] = [score[i] for i in index]
items.reverse()
score.reverse()
## Init plot
plotdata = pd.DataFrame({
    "Score":score
    }, index=items )

ax = plotdata.plot(kind='barh', figsize=(15, 9), color='#e47911', zorder=2, width=0.85)

# Despine
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# Switch off ticks
#ax.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off", labelleft="on")

ax.invert_yaxis()
# Set x-axis label
ax.set_xlabel("Average Score", labelpad=20, size=10)

# Add x, y gridlines
ax.grid(b = True, color ='grey',
        linestyle ='-.', linewidth = 0.5,
        alpha = 0.2)
 

# Add annotation to bars
for i in ax.patches:
    plt.text(i.get_width()+0.2, i.get_y()+0.5,
             str(round((i.get_width()), 2)),
             fontsize = 10, fontweight ='bold',
             color ='grey')
# Format y-axis label
ax.xaxis.set_major_formatter(StrMethodFormatter('{x:,g}'))

plt.subplots_adjust(top=0.960, bottom=0.090, left=0.300, right=0.980)
plt.title("Rankig of Top Score Games")
plt.xticks(rotation=85,fontsize = 9.5)
plt.show()