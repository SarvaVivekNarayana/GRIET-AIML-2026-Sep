import numpy as np

insta_list = []

study_time = []

with open("digital_behaviour.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        insta_list.append(row[APP])
        study_time.append(row["Study Time"])

insta_list = insta_list[:7]
study_time = study_time[:7]

# CONVERT TO NUMPY ARRAYS

insta_array = np.array(insta_list)
study_array = np.array(study_time)

# total = np.sum(insta_array)

total = insta_array.sum()

# average = np.mean(insta_array)
'''average = np.mean(insta_array)

#minimum = np.min(insta_array)
minimum = np.min(insta_array)

maximum = np.max(insta_array)'''

average = insta_array.mean()
minimum = insta_array.min()
maximum = insta_array.max()

#Indexing 

insta_array[0]

insta_array[-1]  #Vectors 

insta_array[0:3]  #Slicing

insta_array[-2::]  #Slicing with step

  
insta_array[1:4]

# insta_array = [val/60 for val in insta_array]

hours = insta_array / 60

diff = insta_array - study_array

# Part G — The security gate (boolean filtering)

# [val>100 for val in insta_array]

greater_than_100 = insta_array > 100

# [val for val in greater_than_100 if val] 

#  [10 , 110, 120, 30 , 50,149, 16 ]

# [f, t, t, f, f, t, f]

greater =  insta_array[insta_array > 100]

count = (insta_array > 100).sum()

greater =  insta_array[insta_array > average]

# Part H — Compare and reflect

# Extend this for all other applications 










