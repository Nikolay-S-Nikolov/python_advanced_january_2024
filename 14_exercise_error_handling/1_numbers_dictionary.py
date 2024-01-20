# Initialize an empty dictionary to store numbers
numbers_dictionary = {}

# Receive input until the command "Search" is encountered
line = input()
while line != "Search":
    # The first line is the number as a text
    number_as_string = line

    try:
        # Receive second line which should be the number as an integer
        number = int(input())
        # Add the pair (number as a text : number as an integer) to the dictionary
        numbers_dictionary[number_as_string] = number

    except ValueError:
        # Print message when the input is not a valid integer
        print("The variable number must be an integer")

    # Get the next line of input
    line = input()

# Receive input until the command "Remove" is encountered
line = input()
while line != "Remove":
    # The line contains the searched number as a text
    searched = line

    try:
        # Try to print the corresponding number from the dictionary
        print(numbers_dictionary[searched])

    except KeyError:
        # Handle the case when the searched number is not in the dictionary
        print("Number does not exist in dictionary")

    # Get the next line of input
    line = input()

# Receive input until the command "End" is encountered
line = input()
while line != "End":
    # The line contains the searched number as a text
    searched = line

    try:
        # Try to remove the searched number from the dictionary
        del numbers_dictionary[searched]

    except KeyError:
        # Handle the case when the number is not in the dictionary
        print("Number does not exist in dictionary")

    # Get the next line of input
    line = input()

# Print the remaining items in the dictionary after processing all commands
print(numbers_dictionary)
