import os, sys
try:
    __import__("m").Main()
except Exception as e:
    exit(str(e))
