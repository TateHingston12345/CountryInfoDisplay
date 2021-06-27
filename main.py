import csv
with open('countries.csv') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  line_count = 0
  r = input('region: ')
  while r != 'quit':
    for row in csv_reader:
      if row == 1:
          print(f'{row[0]}{row[1]}{row[2]}')
      else:
        if r in f'{row[1]}':
          print(f'{row[0]}{row[1]}{row[2]}')
    r = input('region: ')