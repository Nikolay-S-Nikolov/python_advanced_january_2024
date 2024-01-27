import os


def find_files(dir_name, first_level=False):
    for file_or_dir in os.listdir(dir_name):
        file_name = os.path.join(dir_name, file_or_dir)

        if os.path.isfile(file_name):
            file_extension = file_name.split('.')[-1]

            if file_extension not in files_grouped_by_extension:
                files_grouped_by_extension[file_extension] = []

            files_grouped_by_extension[file_extension].append(f"- - - {file_or_dir}")

        elif os.path.isdir(file_name) and not first_level:
            find_files(file_name, first_level=True)


directory = input()
files_grouped_by_extension = {}

try:
    find_files(directory)

except FileNotFoundError:
    WORKING_DIRECTORY_PATH = os.path.dirname(os.path.abspath(__file__))
    searched_path = os.path.join(WORKING_DIRECTORY_PATH, directory)
    print(f"The system cannot find the specified path: {searched_path}")

with open('report.txt', 'w') as report_file:

    for extension, files in sorted(files_grouped_by_extension.items(), key=lambda x: (x[0], x[1])):
        report_file.write(f'.{extension}\n')
        for file in files:
            report_file.write(f'{file}\n')
