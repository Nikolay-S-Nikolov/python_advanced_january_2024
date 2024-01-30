from pyfiglet import figlet_format, print_figlet


def print_art_word(msg):
    ascii_art = print_figlet(msg, font='bubble')
    # font = "5lineoblique" , "3x5" , "3-d", "slant","alphabet", "banner3-D","doh", "isometric1","letters"
    # "bubble", "bulbhead", "digital",
    return ascii_art


# def print_art_with_print_fig(msg):
#     ascii_art = figlet_format(msg)
#     return ascii_art


message = input()

print_art_word(message)
# print(print_art_with_print_fig(message))

# pip install pyfiglet
