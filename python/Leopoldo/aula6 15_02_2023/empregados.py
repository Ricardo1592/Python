import csv
with open() as f:
    reader=csv.reader(f, delimiter=';')
    for l in reader:
        if l[0] == 'id':
            continue