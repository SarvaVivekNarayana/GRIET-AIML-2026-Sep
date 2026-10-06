"""Day 1 Step 2 - CORRECT REFERENCE. Teacher copy. Never released."""
import csv

APP = "Instagram"
minutes = []

with open("digital_behaviour.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        minutes.append(int(row["Instagram_Minutes"]))

minutes = minutes[0:7]

total = 0
for value in minutes:
    total = total + value

average = total / len(minutes)

highest = minutes[0]
for value in minutes:
    if value > highest:
        highest = value

lowest = minutes[0]
for value in minutes:
    if value < lowest:
        lowest = value

count = 0
for value in minutes:
    if value > average:
        count = count + 1

print("App:", APP)
print("Days:", len(minutes))
print("Total Minutes:", total)
print("Average Minutes:", average)
print("Highest Day:", highest)
print("Lowest Day:", lowest)
print("Days Above Average:", count)
