# TODO: A user can enter many names
# TODO: A user can choose to dele a name, based on the name itself
# TODO: A user can choose to exit the system

# 1) to enter a name 2) to delet a name 3) exit
# 1 = Enter name: A

# 1) to enter a name 2) to delete a name 3) exit
# 2 = Enter name to delete: A

# 1) to enter a name 2) to delet a name 3) exit
# 3 = exit

people = []
while True:
  option = input("1. Enter name   2. Delete name   3.Show names  4. Exit")
  if option == "1":
    name = input("Enter name: ")
    person = {
    "name": name,}
    people.append(person)
    print(people)
  elif option == "2":
    delete_name = input("Enter name to be deleted: ")
    for i in range(len(people) -1, -1, -1):
            if people[i]["name"] == delete_name:
                people.pop(i)
                print(i)
  elif option == "3":
    print(people)
  else:
    break









"""
names =[]
while True:
    userinput = input("1) To enter a name. 2) To delete a name 3) Exit 4) Show Names\n")
    if userinput == "1":
        name = input("Enter Name: ")
        names.append(name)
    elif userinput == "2":
        name = input("Enter name to delete: ")
        for i in range(len(names) -1, -1, -1):
            if names[i] == name:
                names.pop(i)
    elif userinput == "3":
        break
    elif userinput == "4":
        print(names)
"""

