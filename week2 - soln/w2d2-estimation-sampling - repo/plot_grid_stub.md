### Starter code for going from one plot to twelve on a grid.

```python
axes = df[months].hist(bins=20, normed=1,
                grid=0, edgecolor='none',
                figsize=(15, 10),
                layout=(3,4))

for month, ax in zip(months, axes.flatten()):
    # you should be able to repurpose the function you wrote to plot 
    # MOM fits to the January data and call it here:
    your_plot_func(df, month)

plt.tight_layout()

# Note that df.hist plots in alphabetical column name order.
# An alternative approach could utilize, e.g.,
# `fig, axes = plt.subplots(4,3, figsize=(15,10))` 
# and
# `ax.hist(df[month], bins=20, normed=1, edgecolor='none')`
```
