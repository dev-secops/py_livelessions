import csv

total = 0.0

with open('data/portfolio.csv', 'r') as file_content:
    rows = csv.reader(file_content)
    headers = next(rows) # skip the heaer row
    for row in rows:
        #line = line.strip() # strip whitespace
        #parts = line.split(',')
        #parts[0] = parts[0].strip('"')
        #parts[1] = parts[1].strip('"')
        row[2] = int(row[2])
        row[3] = float(row[3])
        #print(parts)
        total += row[2]*row[3]

print('Total cost:',total )