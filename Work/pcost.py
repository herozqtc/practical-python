# pcost.py
#
# Exercise 1.27
import os
import gzip

with gzip.open('Work/Data/portfolio.csv.gz','rt') as f:
    next(f) # skip header
    sum = 0.0
    for line in f:
        name, shares, price = line.split(',')
        shares = int(shares)
        price = float(price)
        cost = shares * price
        sum = sum + cost
    f.close()
print('Total cost', round(sum, 2))