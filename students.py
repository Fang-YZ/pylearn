"""
with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")
""" 
"""
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
"""

"""
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")
        
for student in sorted(students):
    print(student)
"""
"""
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        
        #student = {}
        #student["name"] = name
        #student["house"] = house
        
        #以下一行实现上面三行效果
        student = {"name": name, "house": house}
        students.append(student)

def get_name(student):
    return student["name"]  

def get_house(student):
    return student["house"]

for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")

for student in sorted(students, key=get_house, reverse=True):
    print(f"{student['name']} is in {student['house']}")

#lambda表达式，不需要定义函数了，比较简洁    
for student in sorted(students, key=lambda s: s["name"]):
    print(f"{student['name']} is in {student['house']}")"""
    
import csv

students = []

with open("students.csv") as file:
    #reader = csv.reader(file)    #.reader返回列表
    #for row in reader:
    #   students.append({"name": row[0], "home": row[1]})
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"], "house": row["house"]})
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']}, who studies in {student['house']} ,is in {student['home']}")