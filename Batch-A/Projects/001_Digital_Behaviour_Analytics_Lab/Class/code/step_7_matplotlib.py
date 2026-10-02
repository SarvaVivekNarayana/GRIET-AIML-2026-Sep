import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend for plotting

import matplotlib.pyplot as plt

df = pd.read_csv('digital_behaviour.csv')

df['Total_Screen_Time'] = df['Instagram_Minutes'] + df['YouTube_Minutes'] + df['Study_Minutes']

df['day_label'] = [f"Day {i+1}" for i in range(len(df))]

figure(figsize=(12, 6))

bar(df['day_label'], df['Total_Screen_Time'], color='skyblue')

#the whole idea of the parameter order is first what we are comparing, then how much of it, in other words categories then values

title('Total Screen Time per Day')

xlabel('Days')
ylabel('Total Screen Time (minutes)')

xticks(rotation=45)

tight_layout()  # Adjust layout to prevent clipping of tick-labels

savefig('charts/total_screen_time.png')
close()
