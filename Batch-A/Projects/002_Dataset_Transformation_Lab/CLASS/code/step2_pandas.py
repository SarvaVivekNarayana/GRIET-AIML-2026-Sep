import pandas as pd

df = pd.read_csv('day02_usage.csv')

chat = df['Chat'].to_numpy()
video = df['Video'].to_numpy()
study = df['Study'].to_numpy()
games = df['Games'].to_numpy()

print(chat.sum())
print(video.sum())
print(study.sum())
print(games.sum())

print(round(chat.mean(), 1))
print(round(video.mean(), 1))
print(round(study.mean(), 1))
print(round(games.mean(), 1))

diff = study - games

print(diff.argmax())
print(diff.argmin())
