import csv

with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    dates = []
    colors = []
    for row in readCSV:
        color = row[3]
        date = row[0]

        dates.append(date)
        colors.append(color)

    print(dates)
    print(colors)

    #try:

    # now, remember our lists?

##        whatColor = input('What color do you wish to know the date of?:')
##        coldex = colors.index(whatColor)
##        theDate = dates[coldex]
##        print('The date of',whatColor,'is:',theDate)
    #except Exception as e:

list_pt = list('Welcome')
print(list_pt)
x,y=5,6
print(x)
print(y)
