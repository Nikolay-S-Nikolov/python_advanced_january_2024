def sorting_cheeses(**kwargs):
    my_dict = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    result = ""
    for name, quantity in my_dict:
        result += f'{name}\n'
        sorted_quantity = sorted(quantity, reverse=True)
        result += '\n'.join([str(ele) for ele in sorted_quantity])
        result += '\n'

    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
