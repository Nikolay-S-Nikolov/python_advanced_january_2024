from pyfiglet import figlet_format


def print_art_word(msg):
    ascii_art = figlet_format(msg)
    return ascii_art


print(print_art_word(input()))


# pip install pyfiglet
