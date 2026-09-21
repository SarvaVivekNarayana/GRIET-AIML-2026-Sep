import csv
import random as rd
from datetime import datetime, timedelta

#configuration
NO_OF_DAYS = 30

rd.seed()

#create dates
start_date = datetime.now() - timedelta(days=NO_OF_DAYS)

rows = []

for i in range(NO_OF_DAYS):
    current_date = 0
    insta_mins = 1
    youttube_mins = 2
    whasapp_mins = 3
    reels_watched = 4
    linkedin_mins = 5
    videos_watched = 6
    messages_sent = 7
    posts_liked = 8
    study_mins = 9

    rows.append(['current_date', 'insta_mins', 'youtube_mins', 'whatsapp_mins', 'reels_watched', 'linkedin_mins', 'videos_watched', 'messages_sent', 'posts_liked', 'study_mins'])