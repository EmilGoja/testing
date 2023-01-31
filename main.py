import matplotlib.pyplot as plt
import csv

data = []
with open("lee_23.csv",'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        data.append(dict(row))
time = [x['ï»¿Time'] for x in data]
pressure = [x['Pressure'] for x in data]

plt.plot(time,pressure,'co')
plt.show()