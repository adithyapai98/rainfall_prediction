import pandas as pd
#read the source file
df = pd.read_csv('C:/Users/adith/Desktop/Analysis/weather_source.csv',skiprows=3)
#clean the column names
df.columns = df.columns.str.replace('\(.*\)', '',regex=True).str.strip()
#drop time and weathercode columns
data=df.drop(['time','weathercode'],axis=1)
#drop NaN values
data=data.dropna()
#store the processed file in csv format
data.to_csv('C:/Users/adith/Desktop/Analysis/weather_clean.csv',index=False)
