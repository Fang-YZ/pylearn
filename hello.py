"""
def hello(to):
    print("hello,", to)
    


name = input("What's your name? ").strip().title()
hello(name)
print(name)
"""

def main():
    name = input("What's your name? ")
    output = hello(name)
    print(output)

def hello(to="world"):
    return f"hello, {to}"
    
    
if __name__ == "__main__": 
    main()