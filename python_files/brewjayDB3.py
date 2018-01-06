import csv
import re

readBrewery = open('Breweries_v2.csv', 'r')
data = csv.reader(readBrewery)
writeBrewery = open('Breweries_v3.csv', 'w')
writer = csv.writer(writeBrewery)

getRows = []

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)


nullCol = ''
for row in data:
    #row = [value.replace('"', ' ') for value in row]
    getRows.append(row)

for i, row in enumerate(getRows):
    if hasNumbers(getRows[i][3][0])==False:
        last_two = getRows[i][3]
        if last_two[-2:].isupper():

            sliceRows = getRows[i][3:]
            for j, rows in enumerate(sliceRows):
                del getRows[i][3]

            sliceRows = [nullCol] + sliceRows
            for j, rows in enumerate(sliceRows):
                getRows[i].append(sliceRows[j])

writer.writerows(getRows)
