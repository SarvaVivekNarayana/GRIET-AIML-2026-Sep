import csv
import random as rd
from datetime import datetime,timedelta
import re

# config 
NUM_DAYS = 35

rd.seed()

rows=[]



for i in range(NUM_DAYS):
    insta_min = rd.randint(60,14*60)
    youtube_min = rd.randint(10,50)
    whsp_min = rd.randint(40,90)
    lkdin_min = rd.randint(0,20)
    reels_wtch = rd.randint(25,140)

    rows.append( [insta_min,youtube_min,whsp_min,lkdin_min,reels_wtch] )


with open(
    "digital_behaviour.csv",
    "w",
    newline='',
    encoding = "utf-8"
)  as f:
    writer = csv.writer(f)

    writer.writerow(['insta_min','youtube_min','whsp_min','lkdin_min','reels_wtch'])

    writer.writerows(rows)

print("Data generated successfully and saved to digital_behaviour.csv")












