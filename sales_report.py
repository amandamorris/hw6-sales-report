"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.
"""
melon_sales = {}

melon_report = open("sales-report.txt")
for line in melon_report:
    line = line.rstrip()
    entries = line.split("|")
    salesperson = entries[0]
    dollars = entries[1]
    melons_sold = int(entries[2])
    if melon_sales.get(salesperson):
        melon_sales[salesperson]["melons_sold"] += melons_sold
    else:
        melon_sales[salesperson] = {"dollars": dollars, "melons_sold": melons_sold}

for salesperson in melon_sales:
    melons_sold = melon_sales[salesperson]["melons_sold"]
    print "{} sold {} melons.".format(salesperson, melons_sold)

# below here is the bad code we were given, plus my comments on what each line is doing
# salespeople = []
# melons_sold = []

# f = open("sales-report.txt")  # open sales report file
# for line in f:  # for each line...
#     line = line.rstrip()  # strip whitespace from right side of line
#     entries = line.split("|")  # split line into list of components at |
#     salesperson = entries[0]  # 1st element of list is the salesperson
#     melons = int(entries[2])  # 3rd element of list is number of melons

#     if salesperson in salespeople:  # check to see if the salesperson is in the list of SP.  If so...
#         position = salespeople.index(salesperson)  # bind position to the index of the salesperson in the list
#         melons_sold[position] += melons  # increment their melon sales in the same position in the melon list
#     else:  # if not...
#         salespeople.append(salesperson)  # add salesperson to the list
#         melons_sold.append(melons)  # and add their melons sold to the list


# for i in range(len(salespeople)):  # for each salesperson...
#     print "{} sold {} melons".format(salespeople[i], melons_sold[i])  # print "salesperson sold X melons"
