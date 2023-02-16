import csv

with open('empregados.csv') as f:
    reader=csv.reader(f, delimiter=';')