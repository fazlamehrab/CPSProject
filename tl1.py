import pandas as pd
import os,sys

df = pd.read_excel(r'Traffic_Data_City_Square.xlsx')
time = sys.argv[1]
df1 = df[df['Time']==int(time)]
print(df1[["Cars in system","Stops count per car","Average time in system, seconds","Average speed, km/h"]].values.tolist())
