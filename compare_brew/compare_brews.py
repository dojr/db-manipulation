import csv

## csv_analysis python file
## read in a csv file and do some formatting
## extend adds objects in a list
## append appends an object or an item to a list

# Global lists to hold data
get_main_brew = []
get_comp_brew = []
get_beers = []

# read data and puts into globals
def read_get_files():
    readBrewery_og = open('Breweries_v17.csv', 'r')
    readBrewery_new = open('breweries.csv', 'r')
    readBeers = open('beers.csv', 'r')

    main_brew = csv.reader(readBrewery_og)
    comp_brew = csv.reader(readBrewery_new)
    beers = csv.reader(readBeers)

    for row in main_brew:
        get_main_brew.append(row)
    for row in comp_brew:
        get_comp_brew.append(row)
    for row in beers:
        get_beers.append(row)

# returns true if string has numbers
# false otherwise
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def write_files(data):
    write_file = open('Breweries_v18.csv', 'w')
    writer = csv.writer(write_file)
    writer.writerows(data)

def print_data(data):
    for i, rows in enumerate(data):
        print i, data[i]

# removes null columns at end of list
# n represents number of valid cols
def split_null(data, n):
    for i, row in enumerate(data):
        for j, rows in enumerate(data[i]):
            if not rows and j > n:
                data[i] = data[i][:j]
                break;

# returns list of a column in a csv file
# parameters: input data, index of column (zero index)
def get_col(data, n):
    col = []
    for i, row in enumerate(data):
        col.append(data[i][n])
    return col

# strips spaces (default val) from every val in a col
def strip_data(col):
    for i, row in enumerate(col):
        col[i] = col[i].strip()

# tokenize string data from col by char
def split_data(col, char):
    for i, row in enumerate(col):
        col[i] = col[i].strip(char)


read_get_files()
category = get_col(get_beers, 3)
style = get_col(get_beers, 4)
split_null(get_beers, 8)

for i, row in enumerate(get_beers):
    if '-1' in category[i]:
        get_beers[i][3] = 'NULL'

for i, row in enumerate(get_beers):
    if '-1' in style[i]:
        get_beers[i][4] = 'NULL'

print_data(get_beers[:20])

write_file = open('beers_v2', 'w')
writer = csv.writer(write_file)
writer.writerows(get_beers)

# split_null(get_beers, 12)
# address_main = get_col(get_main_brew, 4)
# address_comp = get_col(get_comp_brew, 2)
# name_main = get_col(get_main_brew, 3)
# name_comp = get_col(get_comp_brew, 1)

# save_id_address = []
# for i, row in enumerate(address_comp):
#     if address_comp[i] and address_comp[i] in address_main:
#         print i, address_comp[i]

# for i, row in enumerate(name_comp):
#     if name_comp[i] and name_comp[i] in name_main:
#         print i, name_comp[i]


#print_data(get_main_brew)
# print_data(get_beers)
