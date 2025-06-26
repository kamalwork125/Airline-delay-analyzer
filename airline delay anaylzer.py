import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
#read file
df=pd.read_csv('flights_delay.csv')
print(df)
#line chart
plt.plot(df['Delay(min)'],df["Status"],marker='o',color='pink')
plt.title("comparison between Departure time VS ArrivalTime")
plt.ylabel("Status")
plt.xlabel("Delay(min)")
plt.show()