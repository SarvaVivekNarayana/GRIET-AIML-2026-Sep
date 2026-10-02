#Part A — Bring in the helper

import pandas as pd

#Part B — Load your own data

df = pd.read_csv('digital_behaviour.csv')  

'''
sep = ','
encoding = 'utf-8'
nrows = 400

'''
# Part C — Look before you leap

print(df.head()) 

print(df.tail())

# Returns a tuple (rows,cols)
print(df.shape)

print(df.columns)

 
print(df[["Instagram_Minutes", "Study_Minutes"]].describe())

# df["Instagram_Minutes"]

# Part D — Picking columns

df["Instagram_Minutes"] # series 

col = ["Instagram_Minutes","Study_Minutes"]  

df[col]

df[["date", "Instagram_Mintes"]]  #dataframe

# float f  = 0.1    ISO , IEEE  
# print(f == 0.1)


df["Instagram_Minutes"].sum()

df["Instagram_Minutes"].mean()

round(df["Instagram_Minutes"].mean(), 2)

df["Youtube_Minutes"].max()

val = df[df["Instagram_Minutes"]>100]



# l = [1,2,3,4]
# a,b,c,d = l

# df[True,False,True,False]  # series of boolean values


# df[df["Instagram_Minutes"]>df["Study_Minutes"]]

df[(df["Instagram_Minutes"]>100) & (df["Study_Minutes"]>100)]  # series of boolean values

x,y,z = 10,20,30
x and y and z

x or y or z

df[df["Instagram_Minutes"]>avg]
(df["Instagram_Minutes"]>avg).sum()

s = ["Srikanth","sai","Hi","Ramakrishna"]

s.sort(key=len)

len(s)

sort_values(col_name,ascending=False).head(5)

sort_values(by=["a","b"])

df['Total_Screen_Time'] = (df["Instagram_Minutes"] + df["Youtube_Minutes"] + df["Study_Minutes"])

df["Day_type"]="normal"

df.loc[df["Total_Screen_Time"]>300,"Day_type"]="heavy"

(df['Instagram_Minutes']>300)['Day_type']="heavy"  # wrong

loc[which rows, which columns] = value

df['row']['day_type']

app_totals={
    "Instagram":df["Instagram_Minutes"].sum(),
}

high=max(app_totals,key=app_totals.get)


for key,val in app_totals.items():
    print(f"{key:<6} : {round(val/60,2):>8}")



printf("%3.11s : %.2f", key, val/60);