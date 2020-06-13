# Input CSV, selects counties from list, output data of those counties
import csv
import pandas as pd

df = pd.read_csv('precipitationData.csv', sep=',')

list = ("Food","Food")

# item = 'Nightlife Spots'

# df = df[df['categoryName'].isin(list)]
# df = df[df['categoryName'] == item ]

print(df)

df.to_csv('./temp.csv', index = False, header=True)
