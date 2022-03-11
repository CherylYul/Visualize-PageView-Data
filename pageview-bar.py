# import library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# load data
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=True, index_col=[0])

# clean data
df = df.loc[
    (df["value"] >= df["value"].quantile(0.025))
    & (df["value"] <= df["value"].quantile(0.975))
]

# prepare dataframe
df["month"] = df.index.month
df["year"] = df.index.year
df_bar = df.groupby(["year", "month"])["value"].mean()
df_bar = df_bar.unstack()

# draw bar plot: average daily page views each month grouped by year
fig = df_bar.plot.bar(
    legend=True, figsize=(13, 6), ylabel="Average Page Views", xlabel="Years"
).figure
plt.legend(
    [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
)

plt.xticks(fontsize=8)
plt.yticks(fontsize=8)

fig.savefig("pageview-bar.png")

