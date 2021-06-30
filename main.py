import csv
def region():
  with open('countries.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    r = input('region: ')
    print('------------')
    while r != 'quit':
      for row in csv_reader:
        if r in f'{row[1]}':
          print(f'{row[0]}')
          print(f'{row[1]}')
          print(f'{row[2]}')
          print('------------')
      r = input('region: ')
      print('------------')
    print('program quit')
    print('------------')
region()