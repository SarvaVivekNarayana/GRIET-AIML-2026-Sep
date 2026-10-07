"""Day 1 - Debug Challenge 6 of 6

This one is different.

It does NOT crash.
It prints answers that look completely reasonable.

Your job: decide whether you believe them.
"""
import csv

APP = "Instagram"
minutes = []

with open("digital_behaviour.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        minutes.append(row["Instagram_Minutes"])

minutes = minutes[0:7]

highest = minutes[0]
for value in minutes:
    if value > highest:
        highest = value

lowest = minutes[0]
for value in minutes:
    if value < lowest:
        lowest = value

print("App:", APP)
print("Days:", len(minutes))
print("All values:", minutes)
print("Highest Day:", highest)
print("Lowest Day:", lowest)
