"""
def hello(to):
    print("hello,", to)
    


name = input("What's your name? ").strip().title()
hello(name)
print(name)
"""

def main():
    name = input("What's your name? ")
    hello(name)
    

def hello(to="world"):
    print("hello,", to)
    
main()