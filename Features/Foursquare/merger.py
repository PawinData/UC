# Input CSV, selects counties from list, output data of those counties
import csv
import pandas as pd
import os

path = "./RAW/"

column_names = ['date','county','categoryname','visits']
dfResult = pd.DataFrame(columns = column_names)

entries = []
for file in os.listdir(path):
    if file.endswith(".csv"):
        entries.append(file)

for entry in entries:
	location = path + entry
	print(entry)
	df = pd.read_csv(location)
	# df = df[df.corona == 0]
	# print(df.head(50))
	df = df[df.demo == 'All']

	df = df[['date','county','categoryname','visits']]

	dfResult = pd.concat([dfResult, df]) 

	print(dfResult)

# df = pd.read_csv('visitDataCounties.csv', sep=',')

# list = ("Food","Food")

# item = 'Nightlife Spots'

# # df = df[df['categoryName'].isin(list)]
# df = df[df['categoryName'] == item ]

# print(df)

dfResult.to_csv('./FoursquareData.csv', index = False, header=True)
