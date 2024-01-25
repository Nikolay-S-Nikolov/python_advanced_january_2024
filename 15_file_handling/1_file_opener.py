try:
    file = open('my_dir/text.txt')
    print('File found')
    file.close()
except FileNotFoundError:
    print('File not found')
