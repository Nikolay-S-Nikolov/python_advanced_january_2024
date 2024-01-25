import os

try:
    os.remove('my_file.txt')
except FileNotFoundError:
    print('No such file')
