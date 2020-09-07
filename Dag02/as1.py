#!/usr/bin/env python3.8

from csv import DictReader


total_global_sales = 0

# Read the vgsales file
with open("vgsales.csv") as f:
    for row in DictReader(f):
        # Some computation, that include row["Global_Sales"]
        total_global_sales = "??"

        # more aggregation 
        # ...

# 1.  Find the sum of all global sales (`Global_Sales`)
print("The global sales are {total_global_sales}M")

# 2.  Find all publishers

# 3.  Find the highest grosing publisher

# 4.  Do it by year
