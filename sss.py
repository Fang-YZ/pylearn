import csv

name = input("What's your name? ")
home = input("What's your home? ")

with open("sss.csv", "a",newline="") as file:
    #下面为传入列表
    #writer = csv.writer(file)
    # writer.writerow([name, home])
    
    #下面传入字典,使用DictWriter需决定传入顺序
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})