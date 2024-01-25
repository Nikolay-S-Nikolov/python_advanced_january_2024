import os

WORKING_DIRECTORY_PATH = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(WORKING_DIRECTORY_PATH, 'numbers.txt')

file = open(file_path, 'r')

total = sum(int(x) for x in file)
file.close()
print(total)
