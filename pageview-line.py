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

# draw line plot: time series data
fig = plt.figure(figsize=(15, 7))
plt.figure(figsize=(15, 7))
plt.plot(df, color="red")
plt.xlabel("Date")
plt.ylabel("Page Views")
plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
plt.show()
fig.savefig("pageview-line.png")
