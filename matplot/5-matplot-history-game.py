#!/usr/bin/env python3
import matplotlib.pyplot as plt
import matplotlib.dates as md
import datetime as dt

items = []
scores = []
dates = []
game= None
mTotalReviews=0;
f = open('./5-task/part-00000-wow','r')

for row in f:
    row = row.split('\t')
    if not game:
        game=row[0]
    mTotalReviews+=1
    scores.append(float(row[1]))
    dates.append(int(row[2]))

#Order by unix time (int)
index = list(range(len(dates)))
index.sort(key = dates.__getitem__)
scores[:] = [scores[i] for i in index]
#Parse unix datitime and order dates
dates[:] = [dt.datetime.fromtimestamp(dates[i]) for i in index]


plt.style.use('seaborn')
plt.rcParams["figure.figsize"] = (19,7) 
# Major ticks every 6 months.
fmt_half_year = md.MonthLocator(interval=6)
plt.gca().xaxis.set_major_locator(fmt_half_year)
# Minor ticks every month.
fmt_month = md.MonthLocator()
plt.gca().xaxis.set_minor_locator(fmt_month)  
datenums=md.date2num(dates)
# Text in the x axis will be displayed in 'YYYY-mm' format.
plt.gca().xaxis.set_major_formatter(md.DateFormatter('%d-%m-%Y'))
plt.tight_layout()
# Plot versiont witthout lines
#plt.plot_date(datenums,scores)
plt.plot(datenums,scores,linestyle='solid')
# Rotates and right aligns the x labels, and moves the bottom of the
# axes up to make room for them.
plt.gcf().autofmt_xdate()
plt.xticks(fontsize = 11)
plt.yticks(fontsize = 11)
plt.title('Review History of {0} ({1} reviews)'.format(game,mTotalReviews))
plt.xlabel('Dates',fontsize = 12)
plt.ylabel('Scores',fontsize = 12)
plt.subplots_adjust(top=0.94, bottom=0.265, left=0.09, right=0.94)
plt.show()
