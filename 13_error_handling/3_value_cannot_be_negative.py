class ValueCannotBeNegative(Exception):
    pass


for _ in range(5):
    try:
        num = float(input("Enter a number:"))
        if num < 0:
            raise ValueCannotBeNegative
    except ValueError:
        print("Enter valid number")
