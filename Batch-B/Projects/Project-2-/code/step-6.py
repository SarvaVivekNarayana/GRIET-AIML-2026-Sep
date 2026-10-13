import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")                 
# no display needed
import matplotlib.pyplot as plt

APPS = ["Chat", "Video", "Study", "Games"]
df = pd.read_csv("day02_usage.csv")
usage = df[APPS].to_numpy()
days  = df["Day"].to_numpy()
per_day = usage.sum(axis=1)
shares  = usage / per_day[:, None] * 100

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 8))#axes

for i, app in enumerate(APPS):
    ax1.plot(days, usage[:, i], marker="o", markersize=3, linewidth=1.6, label=app)


# Part B

peak_day = int(per_day.argmax())
ax1.annotate(f"busiest day: {days[peak_day]}",
             xy=(days[peak_day], usage[peak_day].max()),
             xytext=(days[peak_day] + 3, usage[peak_day].max() + 40),
             arrowprops=dict(arrowstyle="->"))

ax1.set_title("Daily minutes per app - 30 days", fontsize=13, fontweight="bold")
ax1.set_xlabel("Day")
ax1.set_ylabel("Minutes")
ax1.legend(ncol=4, frameon=False)
ax1.grid(alpha=0.3)

# Part C

bottom = np.zeros(len(days))
for i, app in enumerate(APPS):
    ax2.bar(days, shares[:, i], bottom=bottom, label=app)
    bottom += shares[:, i]

# \r

ax2.set_title("Share of each day (%) - every bar totals 100", fontsize=12)
ax2.set_xlabel("Day")
ax2.set_ylabel("Share (%)")
ax2.set_ylim(0, 100)
ax2.legend(ncol=4, frameon=False, loc="lower right")

fig.tight_layout()
fig.savefig("day02_usage_chart.png", dpi=130)
print("Saved day02_usage_chart.png")
print("Panel 2 sanity check - row sums:", np.round(shares.sum(axis=1)[:5], 2))

# fig.savefig("abc.png")
