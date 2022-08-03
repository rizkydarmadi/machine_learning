import pandas as pd


# menghitung standar deviasi

x = pd.read_csv('car.csv')
jumlah = len(x['Weight'])
mean = sum(x['Weight'])/jumlah


v1 = 0
for i in x['Weight']:
    v2 = (i - mean)**2
    v1 += v2
v3 = v1 / len(x['Weight'])

import math
print(math.sqrt(v3))
