#name = input("What's your name? ")
#print(f"hello, {name}")
"""
names = []

for _ in range(3):
    names.append(input("What's your name? "))
    
for name in sorted(names):
    print(f"hello, {name}")
"""
"""
name = input("What's your name? ")

#file = open("names.txt", "a")
#file.close()/关闭文件 

# with 自动控制开/关 with ... as ...
with open("names.txt", "a") as file:
    file.write(f"{name}\n")

"""
"""
# 这一段是文件的读取
with open("names.txt", "r") as file:
    lines = file.readlines()
    
for line in lines:
    #print("hello,", line) 
    #print 自动添加换行符
    print("hello,", line.rstrip())
"""
"""
#比较简洁， 不需要显式读取
with open("names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())
"""
"""
names = [] 
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
        
for name in sorted(names):
    print(f"hello,{name}")
"""
names = [] 
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
        
for name in sorted(names, reverse=True):
    print(f"hello,{name}")