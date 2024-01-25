file_path = input('Please enter correct file path: ')

try:
    with open(file_path, 'r') as file:
        print(file.read())
except FileNotFoundError:
    print('Invalid file path')

