import csv
import time


dataFile = "data/data.csv"
header = ["Username", "Favorite"]
Username = ["Test", "Test2", "Test3"]
Favorite = ["True", "False", "True"]
number_user = len(Username)

while True:
    with open(dataFile, "w", newline="") as csv_file:
        writer = csv.writer(csv_file, delimiter=",")
        writer.writerow(header)
        for i in range(number_user):
            writer.writerow([f"{Username[i]}", f"{Favorite[i]}"])

    print("update")
    time.sleep(2)