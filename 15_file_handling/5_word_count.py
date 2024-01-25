import re

words = {}
with open('words.txt', 'r') as file:
    searched_words = file.read().lower().split()

with open('input.txt', 'r') as text_file:
    text_to_search = text_file.read().lower()

for searched_word in searched_words:
    pattern = rf'\b{searched_word}\b'
    result = re.findall(pattern, text_to_search)
    words[searched_word] = len(result)

with open('output.txt', 'w') as f:
    [f.write(f'{k} - {v}\n') for k, v in sorted(words.items(), key=lambda x: -x[1])]
