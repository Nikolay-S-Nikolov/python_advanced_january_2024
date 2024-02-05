import os

WORKING_DIRECTORY_PATH = os.path.dirname(os.path.abspath(__file__))


def create_file(path):
    with open(path, 'w'):
        pass


def add_content(path, data):
    with open(path, 'a') as file:
        file.write(f'{data}\n')


def replace_string(path, *data):
    old_string, new_string = data

    try:
        with open(path, 'r+') as file:
            text = file.read()
            file.seek(0)
            file.write(text.replace(old_string, new_string))

    except FileNotFoundError:
        print("An error occurred")


def delete_file(path):
    try:
        os.remove(path)

    except FileNotFoundError:
        print("An error occurred")


functions = {
    'Create': create_file,
    'Add': add_content,
    'Replace': replace_string,
    'Delete': delete_file
}

command = input().split('-')
while command[0] != 'End':
    action, file_name, *info = command

    try:
        os.mkdir(os.path.join(WORKING_DIRECTORY_PATH, 'files'))
    except FileExistsError:
        pass

    file_path = os.path.join(WORKING_DIRECTORY_PATH, 'files', f'{file_name}')

    functions[action](file_path, *info)

    command = input().split('-')
