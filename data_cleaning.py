import pandas as pd
df = pd.read_csv('C:/Users/adith/Desktop/Analysis/weather_source.csv',skiprows=3)
df.columns = df.columns.str.replace('\(.*\)', '',regex=True).str.strip()
data=df.drop(['time','weathercode'],axis=1)
data=data.dropna()
data.to_csv('C:/Users/adith/Desktop/Analysis/weather_clean.csv',index=False)