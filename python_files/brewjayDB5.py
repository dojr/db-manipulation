import csv

readBrewery = open('Breweries_v17.csv', 'r')
data = csv.reader(readBrewery)
#writeBrewery = open('Breweries_v18.csv', 'w')
#writer = csv.writer(writeBrewery)

getRows = []
nullCol = ''

for row in data:
    getRows.append(row)

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def getState():
    for i, row in enumerate(getRows):
        if getRows[i][4][-2:].isupper()==True:
            state = getRows[i][4].split()[-1]
            getRows[i][4]= getRows[i][4][:-3]
            sliceRows = getRows[i][5:]
            del getRows[i][5:]

            sliceRows= [state] + sliceRows
            for j, rows in enumerate(sliceRows):
                getRows[i].append(sliceRows[j])
            print getRows[i]

#use with Breweries_v10
def seperateWebsite():
    for i, row in enumerate(getRows):
        if getRows[i][7] and '.' not in getRows[i][7]:
            sliceRows = getRows[i][7:]
            sliceRows = [''] + sliceRows
            del getRows[i][7:]
            for j, rows in enumerate(sliceRows):
                getRows[i].append(sliceRows[j])
            print i+1, getRows[i][7], ';', getRows[i][8]

#use with Breweries_v11
def separateWebsite2():
    for i, row in enumerate(getRows):
        if getRows[i][7] and 'com' not in getRows[i][7] and 'www' not in getRows[i][7] and 'ca' not in getRows[i][7] and '/' not in getRows[i][7] and 'org' not in getRows[i][7] and 'net' not in getRows[i][7] and 'beer' not in getRows[i][7]:
            sliceRows = getRows[i][7:]
            sliceRows = [''] + sliceRows
            del getRows[i][7:]
            for j, rows in enumerate(sliceRows):
                getRows[i].append(sliceRows[j])
            print i+1, getRows[i][7], ';', getRows[i][8]

for i, row in enumerate(getRows):
    for j, rows in enumerate(getRows[i]):
        if not rows and j > 8:
            getRows[i] = getRows[i][:j]
            break;
    #print getRows[i]

# for i, row in enumerate(getRows):
#     if getRows[i][8] and hasNumbers(getRows[i][8])==False and 'noon' not in getRows[i][8] and 'Noon' not in getRows[i][8] and 'Open' not in getRows[i][8]:
#         getRows[i][8] = ['']
#     else:
#         op_hours_obj = getRows[i][8:]
#         del getRows[i][8:]
#         getRows[i].append(op_hours_obj)


for i, row in enumerate(getRows):
    if len(getRows[i]) > 9:
        op_hours_obj = getRows[i][9:]
        del getRows[i][8:]
        getRows[i].append(op_hours_obj)
        #print getRows[i][8:]
for i, row in enumerate(getRows):
    print getRows[i]

#writer.writerows(getRows)
