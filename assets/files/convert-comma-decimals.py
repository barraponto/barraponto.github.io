# coding: utf-8
import csv

with open('./tabula-65cdc698f3beab70fb5daa6de6d0d92276872c35.csv') as inputdata,\
    open('./remuneracao-decimais.csv', 'w') as outputdata:

    datawriter = csv.writer(outputdata, dialect='unix')
    for line in csv.reader(inputdata):
        datawriter.writerow([cell.replace(',', '.') for cell in line])
