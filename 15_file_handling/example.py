import os

WORKING_DIRECTORY_PATH = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(WORKING_DIRECTORY_PATH, "my_dir", "my_file.txt")
email = input()

# file = open("text.txt", "w")
file = open(file_path, "w")

# ▪ File modes in Python
# ▪ r - open for reading in text mode -  default value
# ▪ w - open for writing, truncating the file first
# ▪ x - create a new file and open it for writing
# ▪ a - open for writing, appending to the end of the file if it exists
# ▪ t - text mode (default)
# ▪ b - binary mode
# ▪ + - open a disk file for updating (reading and writing)

file.write("Hello")

file.close()

print(email)
