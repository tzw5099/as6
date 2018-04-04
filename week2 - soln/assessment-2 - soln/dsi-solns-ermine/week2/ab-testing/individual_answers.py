# See individual_answers.md for short answer, written responses
# `python individual_answers.py` to run

import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
from itertools import combinations


# Part 2


# 1
alpha = 0.05/23


# 2
df = pd.read_csv('data/nyt1.csv')
df.info()
# Notes: No null types and columns appropriately typed


# 3
df = df[df.Impressions != 0]
df.info()
df['CTR'] = df.Clicks/df.Impressions.astype(float)


# 4
def plot_hist(df, title, color):
    df.hist(figsize=(12, 5), sharey=True, grid=False, color=color, alpha=0.5)
    plt.suptitle(title, size=18, weight='bold')
    plt.tight_layout()
    plt.show()

plot_hist(df, 'Click Through Rate Data', 'g')


# 5
df_signed_in = df[df.Signed_In == 1].copy()
df_not_signed_in = df[df.Signed_In == 0].copy()
df_signed_in.info()
df_not_signed_in.info()

# v0 -- code reuse
plot_hist(df_signed_in, 'Click Through Rate Data for signed in users', 'g')
plot_hist(df_not_signed_in, 'Click Through Rate Data for unknown users', 'b')

# v1 -- a quick and dirty approach
df.groupby('Signed_In').hist(alpha=0.5)
plt.show()

# v2 -- a more satisfying plot
fig, axs = plt.subplots(2, 3, figsize=(12, 5))
for col_name, ax in zip(df_signed_in.columns, axs.flatten()):
    bins = np.linspace(df[col_name].min(), df[col_name].max(), 20)
    ax.hist(df_signed_in[col_name], bins=bins, alpha=0.5,
            normed=1, label="Signed In", color='g')
    ax.hist(df_not_signed_in[col_name], bins=bins, alpha=0.5,
            normed=1, label="Not Signed In", color='b')
    ax.set_title(col_name)
    ax.legend(loc='best')

plt.tight_layout()
plt.show()

# v3 -- an even *more* satisfying plot
fig, axs = plt.subplots(2, 3, figsize=(12, 5))
for col_name, ax in zip(df_signed_in.columns, axs.flatten()):
    bins = np.linspace(df[col_name].min(), df[col_name].max(), 20)
    height, binz = np.histogram(df_signed_in[col_name], bins=bins, normed=1)
    bp1 = ax.bar(bins[:-1], height, .5*(bins[1]-bins[0]),
                 alpha=0.5, label="Signed In", color='g')
    height, binz = np.histogram(df_not_signed_in[col_name], bins=bins, normed=1)
    bp2 = ax.bar(bins[:-1]+.5*(bins[1]-bins[0]), height,
                 .5*(bins[1]-bins[0]), color='b', alpha=.5)
    ax.set_title(col_name)
    ax.legend((bp1[0], bp2[0]), ("Signed In", "Not Signed In"), loc='best')

plt.tight_layout()
plt.show()


# 5
stats.ttest_ind(df_signed_in.CTR, df_not_signed_in.CTR, equal_var=False)


def plot_t_test(group_1_df, group_2_df, group_1_name, group_2_name):
    fig = plt.figure()
    group_1_mean = group_1_df['CTR'].mean()
    group_2_mean = group_2_df['CTR'].mean()

    print '%s Mean CTR: %s' % (group_1_name, group_1_mean)
    print '%s Mean CTR: %s' % (group_2_name, group_2_mean)
    print 'diff in mean:', abs(group_2_mean-group_1_mean)
    p_val = stats.ttest_ind(group_1_df['CTR'], group_2_df['CTR'], equal_var=False)[1]
    print 'p value is:', p_val

    group_1_df['CTR'].hist(normed=True, label=group_1_name, color='g', alpha=0.3)
    group_2_df['CTR'].hist(normed=True, label=group_2_name, color='r', alpha=0.3)
    plt.axvline(group_1_mean, color='r', alpha=0.6, lw=2)
    plt.axvline(group_2_mean, color='g', alpha=0.6, lw=2)

    plt.ylabel('Probability Density')
    plt.xlabel('CTR')
    plt.legend()
    plt.grid('off')
    plt.show()

plot_t_test(df_signed_in, df_not_signed_in, 'Signed In', 'Not Signed In')


# 6
male = df_signed_in[df_signed_in.Gender == 1]
female = df_signed_in[df_signed_in.Gender == 0]
# Note that users *MUST* be signed in to evaluate gender
plot_t_test(male, female, 'M', 'F')


# 7
df_signed_in['age_groups'] = pd.cut(df_signed_in['Age'],
                                    [7, 18, 24, 34, 44, 54, 64, 1000],
                                    include_lowest=True)

df_signed_in['age_groups'].value_counts().sort_index().plot(kind='bar',
                                                            grid=False)
plt.xlabel('Age Group')
plt.ylabel('Number of users')
plt.tight_layout()
plt.show()


# 8
results = pd.DataFrame()
combos = combinations(pd.unique(df_signed_in['age_groups']), 2)
for age_group_1, age_group_2 in combos:
    age_group_1_ctr = df_signed_in[df_signed_in.age_groups == age_group_1]['CTR']
    age_group_2_ctr = df_signed_in[df_signed_in.age_groups == age_group_2]['CTR']
    p_value = stats.ttest_ind(age_group_1_ctr, age_group_2_ctr, equal_var=True)[1]
    age_group_1_ctr_mean = age_group_1_ctr.mean()
    age_group_2_ctr_mean = age_group_2_ctr.mean()
    diff = age_group_1_ctr_mean-age_group_2_ctr_mean
    absolute_diff = abs(age_group_1_ctr_mean-age_group_2_ctr_mean)
    results = results.append({
              'first_age_group':age_group_1, 'second_age_group':age_group_2, 
              'first_group_mean':age_group_1_ctr_mean, 'second_group_mean':age_group_2_ctr_mean,
              'mean_diff':diff, 'absolute_mean_diff':absolute_diff, 'p_value':p_value},
              ignore_index=True)

results = results[['first_age_group', 'second_age_group', 
                   'first_group_mean', 'second_group_mean', 
                   'mean_diff', 'absolute_mean_diff', 'p_value']]
results[results['p_value'] < alpha].sort_values('absolute_mean_diff', ascending=False)
results[results['p_value'] < alpha].sort_values('p_value', ascending=False)
results[results['p_value'] > alpha].sort_values('absolute_mean_diff', ascending=False)
results[results['p_value'] > alpha].sort_values('p_value', ascending=False)
