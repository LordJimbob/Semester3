import csv
with open("custom.csv", encoding= "utf-8") as my_file:
    datareader = csv.reader(my_file, delimiter='¤', quotechar='"')
    print("Users")
    next(datareader)
    for row in datareader:
        print(f"Name: {row[0]}")
        print(f"Last Name: {row[1]}")
        print(f"Note: {row[2]}")
