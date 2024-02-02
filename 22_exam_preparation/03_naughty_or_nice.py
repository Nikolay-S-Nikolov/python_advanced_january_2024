def naughty_or_nice_list(kids_names: list, *args, **kwargs):
    kids_dict = {"Nice": [],
                 "Naughty": []
                 }

    for argument in args:

        command = argument.split('-')
        count = sum(1 for x in range(len(kids_names)) if int(command[0]) == kids_names[x][0])

        if count == 1:
            index = [x for x in range(len(kids_names)) if int(command[0]) == kids_names[x][0]][0]
            kids_dict[command[1]].append(kids_names[index][1])
            kids_names.pop(index)

    for k, v in kwargs.items():
        count = sum(1 for x in range(len(kids_names)) if k == kids_names[x][1])

        if count == 1:
            index = [x for x in range(len(kids_names)) if k == kids_names[x][1]][0]
            kids_dict[v].append(kids_names[index][1])
            kids_names.pop(index)

    if kids_names:
        kids_dict["Not found"] = []
        for kids in kids_names:
            kids_dict["Not found"].append(kids[1])

    result = ''
    for k, v in kids_dict.items():
        if v:
            result += f"{k}: {', '.join(v)}\n"

    return result


print(naughty_or_nice_list([(3, "Amy"), (1, "Tom"), (7, "George"), (3, "Katy"), ], "3-Nice", "1-Naughty", Amy="Nice",
                           Katy="Naughty", ))

print('-----------------------------')
print(naughty_or_nice_list([(7, "Peter"), (1, "Lilly"), (2, "Peter"), (12, "Peter"), (3, "Simon"), ], "3-Nice",
                           "5-Naughty", "2-Nice", "1-Nice", ))
print('-----------------------------')
print(naughty_or_nice_list([(6, "John"), (4, "Karen"), (2, "Tim"), (1, "Merry"), (6, "Frank"), ], "6-Nice", "5-Naughty",
                           "4-Nice", "3-Naughty", "2-Nice", "1-Naughty", Frank="Nice", Merry="Nice", John="Naughty", ))
