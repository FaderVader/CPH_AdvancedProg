from csv import DictReader

total_global_sales = 0
all_publishers = set()

# opgave 1
with open("vgsales.csv") as f:
    for row in DictReader(f):
        value = float(row["Global_Sales"])
        total_global_sales = total_global_sales + value
#print(total_global_sales)

# opgave 2
with open("vgsales.csv") as f:
    for row in DictReader(f):
        publisher = row["Publisher"]
        all_publishers.add(f'{publisher}, ')
#print(len(all_publishers)) # expected count: 579

# opgave 3
highest_global_sales = 0.0
best_publisher = ""
unique_publishers = dict()
with open("vgsales.csv") as f:
    for row in DictReader(f):

        publisher = row["Publisher"]
        global_sales = float(row["Global_Sales"])

        # aggregate sum into dict of publishers
        unique_publishers[publisher] = unique_publishers.get(row["Publisher"], 0) + global_sales

        if global_sales > highest_global_sales:
            best_publisher = publisher
            highest_global_sales = global_sales
print(f'Best publisher: {best_publisher} with {highest_global_sales}')
x = [pub for pub in unique_publishers.items()]
#x.sort()
print(x)
        