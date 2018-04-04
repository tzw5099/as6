import os,sys

import pandas as pd
#import statsmodels.api as sms
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats.kde import gaussian_kde
plt.style.use('bmh')

#####################
## Part 1
#####################

def read_trips_and_preprocess(filename):
    # Read in file
    trips = pd.read_csv(filename, parse_dates=['start_date'])
    start_time = trips['start_date']

    # Get hour, date, dayofweek
    trips['hr'] = start_time.apply(lambda x: x.hour) + 1
    trips['date'] = start_time.apply(lambda x: x.date())    
    trips['dayofweek'] = start_time.apply(lambda x: x.dayofweek + 1) #Monday=1, Sunday=7
    trips['month'] = start_time.apply(lambda x: x.month)
    trips['count'] = 1
    return trips

## use a pickle file to load the data more quickly
from_clean = False
pickle_file = "trip.pickle"
if from_clean or not os.path.exists(pickle_file):
    df = read_trips_and_preprocess('../data/201402_trip_data.csv')
    df.to_pickle(pickle_file)
    print("...saving data to pickle")
else:
    df = pd.read_pickle(pickle_file) 
    print("...data loaded from pickle")

if not os.path.isdir("figs"):
    os.mkdir("figs")
print(df.info())


#####################
## Part 2
#####################

## Group the bike rides by month and count the number of users per month.
month = df['month'].values
month_names = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
month_converter = dict(zip(range(1,13),month_names))
month_inds = {}
print("\n","...rides by month")
for m in range(1,13):
    month_inds[month_converter[int(m)]] = np.where(month==m)[0]
for m in month_names:
    print(m,month_inds[m].size)

## Plot the number of users for each month
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)
ypos = np.arange(len(month_names))
b = ax.barh(ypos,[month_inds[m].size for m in month_names],color='blue')
ax.set_yticks(ypos)
ax.set_yticklabels(month_names)
ax.set_ylabel("month")
ax.set_xlabel("num. rides")
ax.set_title("rides by month")
plt.savefig(os.path.join("figs","users-by-month.png"))

#####################
## Part 3
#####################
## Plot the daily user count from September to December.
## Mark the mean and mean +/- 1.5 * Standard Deviation as horizontal lines 


fig = plt.figure(figsize=(12,10))
ax = fig.add_subplot(111)
date = df['date'].values
count = df['count'].values

for m in ['sep','oct','nov','dec']:
    inds = month_inds[m]
    ploty = [np.where(date[inds]==d)[0].size for d in np.unique(date[inds])]
    plotx = np.unique(date[inds])
    ax.plot(plotx,ploty,marker='o',markersize=6,alpha=0.5)

all_dates = date[np.hstack([month_inds[m] for m in ['sep','oct','nov','dec']])]
unique, all_counts = np.unique(all_dates, return_counts=True)
mean_activity = all_counts.mean()    
upper_std = mean_activity + 1.5 * all_counts.std()
lower_std = mean_activity - 1.5 * all_counts.std()
ax.axhline(upper_std, linestyle='--', c='black', alpha=.4)
ax.axhline(lower_std, linestyle='--', c='black', alpha=.4)
ax.axhline(mean_activity, c='black', alpha=.4)
plt.setp(ax.xaxis.get_majorticklabels(), rotation=90)
plt.savefig(os.path.join("figs","daily-user-count-sept-dec-line.png"))


#####################
## Part 4a
#####################

## Plot the distribution of the daily user counts for all months as a histogram.
## Fit a KDE to the histogram

fig = plt.figure(figsize=(12,10))
ax = fig.add_subplot(111)
unique, all_counts = np.unique(date, return_counts=True)
plotx = np.linspace(0, 1200, 1000)
kde_pdf = gaussian_kde(all_counts)
ploty = kde_pdf(plotx)
ax.plot(plotx, ploty, c='r', lw=2)
ax.hist(all_counts, normed=1, bins=15, edgecolor='none', alpha=.4)
ax.set_ylabel('Probability Density', fontsize=14)
ax.set_xlabel('Number of Users', fontsize=14)
plt.savefig(os.path.join("figs","daily-user-count-histogram.png"))

#####################
## Part 4b
#####################

# Replot the distribution of daily user counts as weekday or weekend rides.
# Refit KDEs onto the weekday and weekend histograms

fig = plt.figure(figsize=(12,10))
ax = fig.add_subplot(111)
dayofweek = df['dayofweek'].values
weekend_unique,weekend = np.unique(date[dayofweek > 5],return_counts=True)
weekday_unique,weekday = np.unique(date[dayofweek <= 5],return_counts=True)
plt.hist(weekend, bins=15, alpha=.1, edgecolor='none', color='g', normed=1)
plt.hist(weekday, bins=15, alpha=.1, edgecolor='none', color='b', normed=1)

# Plotting the KDE of weekday and weekend
kde_pdf = gaussian_kde(weekday)
plotx = np.linspace(min(weekday), max(weekday), 1000)
ploty = kde_pdf(plotx)
ax.plot(plotx, ploty, color='b', lw=2, label='weekday')

kde_pdf = gaussian_kde(weekend)
plotx = np.linspace(min(weekend), max(weekend), 1000)
ploty = kde_pdf(plotx)

ax.plot(plotx, ploty, color='g', lw=2, label='weekend')
ax.set_ylabel('Probability Density', fontsize=14)
ax.set_xlabel('Number of Users', fontsize=14)
ax.legend(frameon=False)

plt.savefig(os.path.join("figs","daily-user-count-histogram-dayofweek.png"))

#####################
## Part 5
#####################

# Make a boxplot of the hours in the day (x) against the number of users (y) in that given hour
def plot_basic_trends(df,ax):
    start_time = df['start_date']
    hr = start_time.apply(lambda x: x.hour) + 1
    date = start_time.apply(lambda x: x.date())    
    dayofweek = start_time.apply(lambda x: x.dayofweek + 1) # Monday=1, Sunday=7
    df['hr'] = hr
    df['date'] = date
    df['dayofweek'] = dayofweek
    df['count'] = 1

    hr = df['hr'].values
    hr_inds = {}
    for h in range(1,25):
        hr_inds[str(h)] = np.where(hr==h)[0]

    toplot = [np.unique(date[hr_inds[str(h)]],return_counts=True)[1] for h in range(1,25)]
    ax.boxplot(toplot)
    ax.set_ylim(0, 200)
    ax.set_xlabel('Hour of the Day', fontsize=14)
    ax.set_ylabel('User Freq.', fontsize=14)

fig = plt.figure(figsize=(12,10))
ax = fig.add_subplot(111)    
plot_basic_trends(df,ax)
plt.savefig(os.path.join("figs","hourly-trends-boxplot.png"))

#####################
## Part 6
#####################
## answer: The variation of the user frequency at each hour in the day over the different days.

#####################
## Part 7 and 8
#####################

#Replot the boxplot in 6. after binning your data into weekday and weekend
#Also explore subscription type: Subscriber and Customer

def set_axis_options(ax, title, txt):
    ax.set_ylim(0, 200)
    ax.set_xlabel('Hour of the Day', fontsize=14)
    ax.set_ylabel('User Freq.', fontsize=14)
    ax.set_title(title)

    ax.text(1,190,txt,color='white',fontsize=14,
            ha="left", va="center",
            bbox = dict(boxstyle="round",facecolor='black',alpha=0.8)
    )
    
def plot_trends2(df, customer_type, axes):
    df = df[df['subscription_type'] == customer_type] # Customer

    hr = df['hr'].values
    hr_inds = {}
    for h in range(1,25):
        hr_inds[str(h)] = np.where(hr==h)[0]

    date=df['date'].values    
    dayofweek = df['dayofweek'].values    
    weekend_inds = np.where(dayofweek > 5)[0]
    weekday_inds = np.where(dayofweek <= 5)[0]

    def get_inds(h,dtype):
        if dtype=='wd':
            return (np.intersect1d(hr_inds[str(h)],weekday_inds))
        elif dtype=='we':
            return (np.intersect1d(hr_inds[str(h)],weekend_inds))
        else:
            raise Exception("bad dtype given")
    
    wkday_lst = [np.unique(date[get_inds(h,'wd')],return_counts=True)[1] for h in range(1,25)]
    wkend_lst = [np.unique(date[get_inds(h,'we')],return_counts=True)[1] for h in range(1,25)]
        
    axes[0].boxplot(wkday_lst)
    axes[1].boxplot(wkend_lst)
    set_axis_options(axes[0], 'Weekday', customer_type)
    set_axis_options(axes[1], 'Weekend', customer_type)
    plt.tight_layout()

fig = plt.figure(figsize=(12,10))
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

plot_trends2(df,'Subscriber',(ax1,ax2))
plot_trends2(df,'Customer',(ax3,ax4))
plt.savefig(os.path.join("figs","hourly-trends-by-subscription.png"))
plt.show()
