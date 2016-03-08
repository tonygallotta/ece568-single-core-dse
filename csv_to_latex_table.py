import csv

with open("results.csv") as csvfile:
  reader = csv.reader(csvfile, delimiter=',')
  # skip header row
  next(reader, None)
  for row in reader:
    row[3] = str(round(float(row[3]), 2))
    print " & ".join(row) + " \\\\ \hline"
