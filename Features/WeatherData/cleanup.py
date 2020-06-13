# Input CSV, turns Google Earth Engine Data into data usable for our pipeline.
import csv
import pandas as pd

df = pd.read_csv('precipitationData.csv')

df['date'] = pd.to_datetime(df['date'], dayfirst = False, yearfirst = False)

df = df.groupby('date').sum().reset_index()

print(df)



df.to_csv('./precipitationData2.csv', index = False, header=True)
