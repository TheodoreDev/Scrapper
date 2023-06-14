import csv

dataFile = "data/data.csv"
header = ["Username", "Favorite"]


with open(dataFile, "w", newline="") as csv_file:
    writer = csv.writer(csv_file, delimiter=",")
    writer.writerow(header)
    writer.writerow(["Test", "True"])
    writer.writerow(["test2", "False"])
    writer.writerow(["test3", "True"])

