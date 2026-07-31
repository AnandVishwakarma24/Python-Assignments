# Python Fundamentals

# (Assignment5)

# Assignment Problems



# Q1. Create a program that:
# 1. Opens a file "names.txt" in write mode
# 2. Writes 5 names (one per line) entered by the user
# 3. Then opens the same file in read mode and prints all names


# with open("name.txt","w") as f:
#     for i in range(0,5):
#         name=input(f"Enter name {i+1} : ")
#         f.write(name+"\n")
# with open("name.txt","r") as f:
#     print(f.read())



# Q2. Create a program that:
# 1. Opens a file "log.txt" in append mode
# 2. Adds a new log entry (like "Program run successfully")
# 3. Opens the file in read mode and prints all logs


# with open("log.txt","a+") as f:
#     f.write("\n Program run successfully")
# with open("log.txt","r") as f:
#     print(f.read())



# Q3. Create a program that:
# 1. Has a list of numbers: [5, 10, 15, 20, 25]
# 2. Uses a list comprehension to create a new list with only numbers greater than 15
# 3. Prints the new list


# lst=[5,10,15,20,25]
# new_list=[ i for i in lst if (i>15)]
# print(new_list)



# Q4. Create a Python dictionary of 3 cities and their populations. Save it to "cities.json"
# 1. Then load the JSON and print each city and its population.
# 2. Ask the user for a new city & its population - update this info in the json
# file.


# import json
# cities={
#     "Silvass":10000,
#     "Delhi":200000,
#     "Mumbai":150000
# }

# with open("cities.json", "w") as f:
#     json.dump(cities, f)
# with open("cities.json","r") as f:
#     data=json.load(f)
# for city, population in data.items():
#     print(f"{city} : {population}")
# new_city=input("Enter new city name : ")
# new_population=input("Enter new population : ")
# data[new_city]=new_population
# with open("cities.json","w")as f:
#           json.dump(data,f,indent=4)
# print(f"Updated Data : {data}")



# Q5. Write a program that tries to open "data.txt" in read mode. If the file does not
# exist, catch the exception and print "File not found!".


# try:
#     with open("data.txt","r") as f:
#         print(f.read())
# except FileNotFoundError:
#     print("File not found!")
