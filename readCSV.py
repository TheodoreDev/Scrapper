import csv
import time

dataFile = "data/data.csv"


with open(dataFile, "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        print(line)
    print("************************************************************")
time.sleep(5)