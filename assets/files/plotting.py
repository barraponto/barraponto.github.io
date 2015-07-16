# coding: utf-8
import csv
from collections import defaultdict

class Wage(object):
    def __init__(self, data):
        self.value = float(data.strip())
        self.hist_bin = int(self.value // 788)

hist = defaultdict(list)
with open('./remuneracao-decimais.csv') as datafile:
    reader = csv.reader(datafile)
    for line in reader:
        wage = Wage(line[1])
        hist[wage.hist_bin].append(wage.value)

plot_sum = {hist_bin: sum(paychecks) for hist_bin, paychecks in hist.items()}
plot_count = {hist_bin: len(paychecks) for hist_bin, paychecks in hist.items()}

with open('sumplot.csv', 'w') as plotfile:
    writer = csv.writer(plotfile)
    writer.writerows(plot_sum.items())

with open('countplot.csv', 'w') as plotfile:
    writer = csv.writer(plotfile)
    writer.writerows(plot_count.items())
