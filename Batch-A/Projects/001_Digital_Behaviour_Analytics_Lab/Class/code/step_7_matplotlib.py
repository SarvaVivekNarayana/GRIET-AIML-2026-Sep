'''import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend for plotting

import matplotlib.pyplot as plt

df = pd.read_csv('digital_behaviour.csv')

df['Total_Screen_Time'] = df['Instagram_Minutes'] + df['YouTube_Minutes'] + df['Study_Minutes']

df['day_label'] = [f"Day {i+1}" for i in range(len(df))]

plt.figure(figsize=(12, 6))

plt.bar(df['day_label'], df['Total_Screen_Time'], color='skyblue')

#the whole idea of the parameter order is first what we are comparing, then how much of it, in other words categories then values

plt.title('Total Screen Time per Day')

plt.xlabel('Days')
plt.ylabel('Total Screen Time (minutes)')

plt.xticks(rotation=45)

plt.tight_layout()  # Adjust layout to prevent clipping of tick-labels

plt.savefig('charts/total_screen_time.png')

plt.close()

plt.plot(df['day_label'], df['Study_Time'], marker='o', label='study' , color='b')

plt.legend()

plt.pie(totals, labels=totals.keys(), autopct='%1.1f%%', startangle=90)'''

import pandas as pd

import matplotlib 
matplotlib.use('Agg')

import matplotlib.pyplot as plt

df=pd.read_csv('./digital_behaviour.csv')

df['Total_Screen_Time'] = df['Instagram_Minutes']+df['YouTube_Minutes']+df['LinkedIn_Minutes']+df['Whatsapp_Minutes']

df['day_label'] = [f"Day {i+1}" for i in range(len(df))]

plt.figure(figsize=(12,6))

plt.bar(df['day_label'], df['Total_Screen_Time'], color='blue')

plt.title('Screen Time per day')

plt.xlabel('Days')
plt.ylabel('Total Sreen Time')

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('chars/total_screen_time.png')  

plt.close()

apps = ['Intagram', 'Whatsapp' 'YoutTube', 'LinkedIn']

totals = [
    df['Instagram_Minutes'].sum(),
    df['Whatsapp_Minutes'].sum(),
    df['YouTube_Minutes'].sum(),
    df['LinkedIn_Minutes'].sum()
]
plt.figure(figsize=(12,6))

plt.bar(apps, totals, color=["#E1306C", "#FF0000", "#25D366", "#0A66C2"])

plt.savefig('chars/app_screen_time.png')

plt.close()

plt.figure(figsize=(12,5))

plt.plot(df['day_label'], df['Study_Time'], marker='o', label='study', color='pink')
plt.plot(df['day_label'], df['Total_Screen_Time'], marker='s', label='Screen Time', color='blue')

plt.legend()

plt.close()

plt.figure(figsize=(5,5))

plt.pie(totals, labels=apps, autopct='%1.1f%%', colors=["#E1306C", "#FF0000", "#25D366", "#0A66C2"])

plt.savefig('chars/tital_screen_time.png')

plt.close()