with open("write_to_csv.csv", "a", encoding="utf-8") as my_file:
    while True:
        name = input("Enter Name: ")
        last_name = input("Enter Last Name: ")
        my_file.write(f"\n{name}¤{last_name}")