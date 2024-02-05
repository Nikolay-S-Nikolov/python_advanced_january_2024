name = []
for element in input().split():
    letter = ''
    for symbol in element:
        if symbol.isdigit():
            letter += symbol
        elif symbol.isalpha():
            if symbol.isupper():
                symbol = symbol.lower()
            letter += symbol
    if letter:
        name.append(letter)
print('_'.join(name))


