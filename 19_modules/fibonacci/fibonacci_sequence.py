def create_sequence(num):
    if num == 0:
        return ''
    elif num == 1:
        return 0
    else:
        result = [0, 1]
        for n in range(num - 2):
            result.append(result[-1] + result[-2])
        return result


def locate_num(number: int, sequence: list):
    try:
        index = sequence.index(number)
        print(f"The number - {number} is at index {index}")
    except ValueError:
        print(f"The number {number} is not in the sequence")


