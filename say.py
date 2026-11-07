"""
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.turkey("hello, " + sys.argv[1])
"""
import sys
from saying import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])