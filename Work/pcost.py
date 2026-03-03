# pcost.py
#
# Exercise 1.27
import os
import sys
import gzip

def sumcount(filename):
    with open(filename,'rt') as f:
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

if len(sys.argv) == 2:
    filename = sys.argv[1]
    if os.path.isfile(filename):
        sumcount(filename)
    else:
        print('File not found:', filename)