import pandas as pd
import numpy as np

df = pd.read_csv('day02_usage.csv')

chat = df['Chat'].to_numpy()
video = df['Video'].to_numpy()
study = df['Study'].to_numpy()
games = df['Games'].to_numpy()

print("Total minutes over the thirty days:" , chat.sum() , video.sum() , study.sum() , games.sum())

#mean round to 1 decimal places
print("Mean minutes over the thirty days:" , round(chat.mean(), 1) , round(video.mean(), 1) , round(study.mean(), 1) , round(games.mean(), 1))
    
#Part C — One derived measure
balance = study - games

print(f"best day for study vs games: {int(balance.argmax())+1} with a balance of {balance.max()} minutes")

#Part D — Now the question changes direction
#D1 which app won each day
names = ["Chat", "Video", "Study", "Games"]
winners = []
for i in range(len(chat)):
    day_values = [chat[i], video[i], study[i], games[i]]   
    # rebuild a row by hand
    best = 0
    for j in range(1, 4):
        if day_values[j] > day_values[best]:
            best = j
    winners.append(names[best])

#D2. What share of each day did each app take?    
    total = sum(day_values)
    if total > 0:
        shares = [round(v / total, 2) for v in day_values]
    else:
        shares = [0, 0, 0, 0]
    print(f"Day {i+1}: {names[0]}={shares[0]}, {names[1]}={shares[1]}, {names[2]}={shares[2]}, {names[3]}={shares[3]}")