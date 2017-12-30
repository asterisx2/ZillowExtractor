import csv;

def saveToCsv(path, data):
    writer = csv.writer(open(path, 'w'))
    for row in data:
            writer.writerow(row)
