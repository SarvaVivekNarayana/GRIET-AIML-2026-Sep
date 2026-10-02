''''''#app name
APP = "Instagram"

minutes = []

with open("digital_behaviour.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        minutes.append(row[im])


# minutes[start:stop:step]

minutes[:7]

# ADDITION
total = sum(minutes)

# AVERAGE VALUE
average = total/len(minutes) 

# MAXIMUM VALUE


# MINIMUM VALUE


# COUNT VALUES > A
counter = 0

for i in minutes :
    if i > average :
        counter+= 1

# PRINT THE VALUES

"""PRINT THE APP NAME , TOTAL , AVG , MAX , MIN , COUNTER , 
   IN ONE LINE USING 'f' STRINGS
"""


    



'''

# PROGRAM 1 NUMPY FILE

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
average = insta_array.mean()

#minimum = np.min(insta_array)
minimum = np.min(insta_array)

maximum = np.max(insta_array)





help(insta_array)
  
'''

'''
s = "GRIET College Nizampet Hyderabad"
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

s.upper().reverse().casefold() #Operator chaining

ans = s.split().upper()

#    TEIRG EGELLOC TEPMAZIN DABAREDYH 

#Iterables 

for i in ["abc", "def", "ghi"]: 


yield'''

'''Ellipsis
...

public static void main(String...args) 

Spread Operator (JavaScript)

Packing and Unpacking (Python)


Filter Function

s = "GRIET College Nizampet Hyderabad"

filtered = filter(lambda x: x.isalpha(), s.split())

print( " ".join(word[::-1] for word in input().split()) )'''



s = [int(num) for num in input().split() if num&1]  # num&1 Binary Operaotor to check odd numbers

s = list(filter(lambda x: x%2, [int(num) for num in input().split()])) 

#lamda functions are anonymous functions
















