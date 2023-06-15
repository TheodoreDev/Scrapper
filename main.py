import csv
import time


while True:
    dataFile = "data/data.csv"
    header = ["Country", "Inhabitants"]
    Country = ["Test", "Test2", "Test3"]
    Inhabitants = ["1000", "120", "3500"]
    number_user = len(Country)

    with open(dataFile, "w", newline="") as csv_file:
        writer = csv.writer(csv_file, delimiter=",")
        writer.writerow(header)
        for i in range(number_user):
            writer.writerow([f"{Country[i]}", f"{Inhabitants[i]}"])

    print("update")
    time.sleep(2)