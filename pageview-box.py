# import library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load data
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=True, index_col=[0])

# clean data
df = df.loc[
    (df["value"] >= df["value"].quantile(0.025))
    & (df["value"] <= df["value"].quantile(0.975))
]

# prepare data
df_box = df.copy()
df_box.reset_index(inplace=True)
df_box["year"] = [d.year for d in df_box.date]
df_box["month"] = [d.strftime("%b") for d in df_box.date]

# draw the boxplot: distribution of page views
df_box["month_num"] = df_box["date"].dt.month
df_box = df_box.sort_values("month_num")

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))
ax[0] = sns.boxplot(x=df_box["year"], y=df_box["value"], ax=ax[0])
ax[1] = sns.boxplot(x=df_box["month"], y=df_box["value"], ax=ax[1])

ax[0].set_title("Year-wise Box Plot (Trend)")
ax[0].set_xlabel("Year")
ax[0].set_ylabel("Page Views")

ax[1].set_title("Month-wise Box Plot (Seasonality)")
ax[1].set_xlabel("Month")
ax[1].set_ylabel("Page Views")

fig.savefig("pageview-box.png")

