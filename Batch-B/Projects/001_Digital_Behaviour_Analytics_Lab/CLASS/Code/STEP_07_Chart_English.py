import pandas as pd
import matplotlib   
matplotlib.use('Agg')  
import matplotlib.pyplot as plt

df = pd.read_csv("digital_behaviour.csv")


df["Total_Screen_Time"] = (
    df["Instagram_Minutes"] + df["YouTube_Minutes"]
    + df["WhatsApp_Minutes"] + df["LinkedIn_Minutes"]
)

df["Day_Label"] = [f"D{i+1}" for i in range(len(df))]

# labels = []
# for i in range(len(df)):
#     labels.append(f"D{i+1}")

#PART B: Create a bar chart to visualize the total screen time over days

plt.figure(figsize=(10, 6))

plt.bar(df["Day_Label"], df["Total_Screen_Time"], color='skyblue')

plt.title("Total Screen Time Over Days")
plt.xlabel("Days")
plt.ylabel("Minutes") 
plt.xticks(rotation=45)  
plt.tight_layout()
plt.savefig("total_screen_time_chart.png")
plt.close()


#PART C Chart 2: Where does the time go?




