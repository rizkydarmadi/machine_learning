import researchzky 
import csv

file = open('/home/rizkyd/course/python/machine_learning/linear-regresion/dataset/data_handpone.csv')
type(file)
csvreader = csv.reader(file)
header = []
header = next(csvreader)
rows = []
for row in csvreader:
    rows.append(row)

data = []
for i in rows:
    if i[2] == '':
        continue
    data.append([int(i[1]),int(i[2])])


sample = researchzky.SimpleLinearRegresion(data=data)
researchzky.SimpleLinearRegresion.show(sample,x=8)
