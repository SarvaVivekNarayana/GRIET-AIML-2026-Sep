import pandas as pd
import numpy as np

#A — Build the table
df = pd.read_csv('day02_usage.csv')

#apps = df.columns
apps=['Chat','Video','Study','Games']


data = df[apps].to_numpy()
print(data.shape)

#B — The direction dial
app_totals=data.sum(axis=0)
day_totals=data.sum(axis=1)

app_means=data.mean(axis=0)
day_means=data.mean(axis=1)

app_min = data.min(axis=0)
day_min = data.min(axis=1)

app_max = data.max(axis=0)
day_max = data.max(axis=1)

#C — Kill the nine-line loop
names = np.array(apps)
#names = ['Chat','Video','Study','Games']

'''x = data.argmax(axis=1)
x=[3,2,0,1,3,1,0,2,1,3]
names[[3,2,0,1,3,1,0,2,1,3]]
winningapp_perday = names[x]
#['Video', 'Video', ...]'''

winners = names[data.argmax(axis=1)]

unique, counts = np.unique(winners, return_counts = True)
d=dict(zip(unique,counts.tolist())).items()

print(*d,sep='\n')

#D — Broadcasting: a table divided by a column

per_day = data.sum(axis=1)
#shares = data / per_day
shares = data / per_day[:,None] * 100

print(np.round(shares.mean(axis=0),1))

#(30,)
#(30,1)
print(per_day.shape)
print(per_day[:,None].shape)

per_app_max = data.max(axis=0)
#per_app_max.shape -> (4,)
scale = data/per_app_max

#(30,4)/(4,)
#(30,4)/(30,)
#(30,4)/(30,1)

#E — Questions you could not ask before
weekend_mask = (df['Day'] % 6 == 0 | df['Day'] % 7 == 0)

np.round(data[weekend_mask].mean(axis=0),1)

np.round(data[~weekend_mask].mean(axis=0),1)

print(per_day.argmax()+1,per_day.max())