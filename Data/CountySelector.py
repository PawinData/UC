# Input CSV, selects counties from list, output data of those counties
import csv
import pandas as pd

df = pd.read_csv('visitData.csv', sep=',')

list = ("San Francisco County", "Alameda County", "Contra Costa County", "Marin County", "Napa County", 
"San Mateo County", "Santa Clara County", "Solano County", "Sonoma County")

df = df[df['county'].isin(list)]
print(df)

df.to_csv('./visitDataCounties.csv', index = False, header=True)
