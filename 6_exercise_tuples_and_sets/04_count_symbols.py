text = input()
unique_symbols = set()
symbol_dict = {}

for symbol in input():
    unique_symbols.add(symbol)

for sym in unique_symbols:
    symbol_dict[sym] = text.count(sym)

for k, v in sorted(symbol_dict.items()):
    print(f'{k}: {v} time/s')

# Solution 2
# symbol_dict = {}
#
# for symbol in input():
#     symbol_dict[symbol] = symbol_dict.get(symbol, 0) + 1
#
# for sym, occurrences in sorted(symbol_dict.items()):
#     print(f'{sym}: {occurrences} time/s')


# Solution 3
# text = input()
#
# for symbol in sorted(set(text)):
#     print(f'{symbol}: {text.count(symbol)} time/s')
