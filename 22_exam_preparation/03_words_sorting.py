def words_sorting(*words):
    words_dict = {}

    for word in words:
        words_dict[word] = sum(ord(x) for x in word)

    sum_of_all_value = sum(v for v in words_dict.values())

    if sum_of_all_value % 2 == 0:
        sorted_dict = sorted(words_dict.items(), key=lambda kvp: kvp[0])

    else:
        sorted_dict = sorted(words_dict.items(), key=lambda kvp: -kvp[1])

    result = ''
    for key, value in sorted_dict:
        result += f"{key} - {value}\n"

    return result


print(words_sorting('escape', 'charm', 'mythology'))
print(words_sorting('escape', 'charm', 'eye'))
print(words_sorting('cacophony', 'accolade'))
