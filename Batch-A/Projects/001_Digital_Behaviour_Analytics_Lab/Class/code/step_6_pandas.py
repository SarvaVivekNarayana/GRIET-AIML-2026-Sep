import pandas as pd

'''dataframe - collection of all rows and columns
series - for columns
index - no. of rows'''

#Part B — Load your own data
df = pd.read_csv('digital_behaviour.csv')

#sep, encoding, nrows
'''
head()
tail()
colunmn
shape
'''

#C
'''float f = 0.1
f == 0.1'''

#Part C — Look before you leap
print(df.head())
print(df.tail())
print(df.shape)
print(list(df.columns))

col_name=['insta_minutes','study_minutes']
df[col_name].describe()

#df[['insta_minutes','video']].describe()

#Part E — Column maths, no loop
df['insta_minutes'].sum()
round(df['study_minutes'].mean(),2)
df['youtube_minutes'].max()

#Part F — The security gate, on a table (filtering)
df[df['insta_minutes']>100]
df[df['study_minutes']>180]
df[df['study_minutes']<df['insta_minutes']]

'''danger_days = df[
    (df["Instagram_Minutes"] > 100) & (df["Study_Minutes"] < 100)
]'''
'''x,y,z=10,20,30
print(x and y and z)
print(x or y or z)'''

&
|
~
()

#Part G — Sorting
top_insta = df.sort_values("Instagram_Minutes", ascending=False).head(10)

top_study = df.sort_values("Study_Minutes", ascending=False).head(10)

#Part H — Creating new knowledge
df['Total_Screen_Time'] = (df['insta_minutes'] + df['study_minutes'] + df['youtube_minutes'])

'''names=['PS':'Veda','SS':'Ravi','AS':'Sita','RS':'Kiran','VS':'Anil','MS':'Priya','VS':'Ramesh','PS':'Vikram','SS':'Neha','AS':'Amit']
names['MS']='Geeta'
names['KS']='Krish'''

df['Screen_Hours']=(df['Total_Screen_Time']/60).round(2)

df['Digital_Balance']=(df['study_minutes']/df['Total_Screen_Time']).round(2)

#df.loc[which row, which column]
df["Day_Type"] = "Normal"
df.loc[df["Total_Screen_Time"] > 300, "Day_Type"] = "Heavy"

#mask
df[df['Total_Screen_Time']>300]['Day_Type'] = 'Heavy'

df['Day_Type'].value_counts()

app_totals = {
    "Instagram": df["Instagram_Minutes"].sum(),
}

max_time = max(app_totals, key=app_totals.get)

'''s=['veda','hi','swapna']
max(s,key=len)

max_len = ''
for word in s:
    if len(word) > len(max_len):
        max_len = word'''

heavy_day = df.loc[df['Total_Screen_Time'].idxmax()]

study_day = df.loc[df['Total_Screen_Time'].idxmax(),['study_minutes']]

'''sum=0
for key in app_totals:
    sum+=app_totals[key]
print(sum/len(app_totals))'''

for app,minutes in app_totals.items():
    print(f"{app:<10.15} : {minutes:>6} min ({round(minutes/60, 1)} hours)")

   ''' printf("%<4.6s : %d min %.1f hours",app, minutes, minutes/60)
    hi  
      hi
     hi '''

'''s = ""
scanf("%[a-z]",&s)
print(s)'''