import csv

STEP = 4


def get_cities():
    with open('ok_cities.csv', 'rb') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        rows = [row[0] for row in reader]

        return [rows[i: i + STEP] for i in xrange(0, len(rows), STEP)]
