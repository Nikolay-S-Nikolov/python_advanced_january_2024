def grocery_store(**product_quantity):
    sorted_dict = dict(sorted(product_quantity.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
    return '\n'.join([f"{product}: {quantity}" for product, quantity in sorted_dict.items()])


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

print("\n----------\n")

print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
