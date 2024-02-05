import os

WORKING_DIRECTORY_PATH = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(WORKING_DIRECTORY_PATH, 'files', 'text.txt')

symbols = ["-", ",", ".", "!", "?"]

with open(file_path) as file:
    text = file.readlines()

for row in range(0, len(text), 2):

    for symbol in symbols:
        text[row] = text[row].replace(symbol, '@')

    print(*text[row].split()[::-1])
