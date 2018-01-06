import csv
import re

readBrewery = open('Breweries.csv', 'r')
#writeBrewery = open('Breweries_v2.csv', 'w')
data = csv.reader(readBrewery)
#writer = csv.writer(writeBrewery)

get3rdEle = []

for row in data:
    #row = [value.replace('"', ' ') for value in row]
    get3rdEle.append(row)

createData = []
for i, row in enumerate(get3rdEle):
    createData.append(get3rdEle[i][3])

for i, rows in enumerate(createData):
    createData[i] = createData[i].strip().split(",")

#print createData[0][1].strip()
for i, rows in enumerate(createData):
    for j, index in enumerate(createData[i]):
        createData[i][j] = index.strip()

for i, rows in enumerate(get3rdEle):
    del get3rdEle[i][3]
    get3rdEle[i].extend(createData[i])


#writer.writerows(get3rdEle)
