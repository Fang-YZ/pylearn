name = input("What's your name? ")

name = name.strip().title()

print(f"hello, {name}")

print("hello", name)

first, last = name.split(" ")

print("hello", first)