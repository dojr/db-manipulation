import csv
import re
import string

readBrewery = open('Breweries_v5.csv', 'r')
data = csv.reader(readBrewery)

writeBrewery = open('Breweries_v6.csv', 'w')
writer = csv.writer(writeBrewery)

getRows = []

for row in data:
    getRows.append(row)

for i, row in enumerate(getRows):
    last_two = getRows[i][4]
    first_two = getRows[i][5]
    if last_two[-2:].isupper()==False and first_two.isupper()==False and "(" in last_two and any(c.isalpha() for c in last_two)==False:
            # token = getRows[i][4].split()
            # token[-1]
            # sliceRows = getRows[i][5:]
            # del getRows[i][5:]
            # getRows[i].append(token[-1])
            # for j, rows in enumerate(sliceRows):
            #     getRows[i].append(sliceRows[j])
            # state = ' '.join(token[0:2])
            # getRows[i][4] = state
            print i, getRows[i][3:6]

#writer.writerows(getRows)
