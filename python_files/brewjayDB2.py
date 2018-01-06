import csv
import re

readBrewery = open('Breweries.csv', 'r')
# writeBrewery = open('Breweries2.csv', 'w')
data = csv.reader(readBrewery)
# writer = csv.writer(writeBrewery)

rows = []

for row in data:
    #row = [value.replace('"', ' ') for value in row]
    rows.append(row)

createData = []
createData = rows[0][3]
split = createData.strip().split(",")

for i, row in enumerate(split):
    split[i] = row.strip()

createData = split

print createData

del rows[0][3]

rows[0].extend(createData)
print rows[0]
