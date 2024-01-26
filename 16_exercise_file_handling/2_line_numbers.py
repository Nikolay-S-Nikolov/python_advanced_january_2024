import os
from string import punctuation

WORKING_DIRECTORY_PATH = os.path.dirname(os.path.abspath(__file__))
file_path_text_txt = os.path.join(WORKING_DIRECTORY_PATH, 'files', 'text.txt')
file_path_output_txt = os.path.join(WORKING_DIRECTORY_PATH, 'files', 'output.txt')

with open(file_path_text_txt) as file:
    text = file.readlines()

output_file = open(file_path_output_txt, 'w')

for idx in range(len(text)):
    letters, marks = 0, 0

    for symbol in text[idx]:
        letters += 1 if symbol.isalpha() else 0
        marks += 1 if symbol in punctuation else 0

    output_file.write(f"Line {idx + 1}: {text[idx][:-1]} ({letters})({marks})\n")

output_file.close()