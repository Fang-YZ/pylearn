import sys
"""
print(sys.version)
print(sys.path)
"""
"""
try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")
"""
"""
if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])    
"""
if len(sys.argv) < 2:
    sys.exit("Too few arguments")

#-1 为反向计数，最后一个数省略
for arg in sys.argv[1:-1]:
    print("hello, my name is", arg)