def shopping_cart(*products):

    products_limit = {
        'Soup': 3,
        'Pizza': 4,
        'Dessert': 2
    }

    products_in_cart = {
        'Soup': [],
        'Pizza': [],
        'Dessert': []
    }

    for list_item in products:

        if list_item == 'Stop':
            break

        meal, product = list_item

        if products_limit[meal] and product not in products_in_cart[meal]:
            products_limit[meal] -= 1
            products_in_cart[meal].append(product)

    if products_in_cart["Soup"] or products_in_cart["Pizza"] or products_in_cart["Dessert"]:

        result = ''
        for meal_type, sorted_product in sorted(products_in_cart.items(), key=lambda x: (-len(x[1]), x[0])):
            result += f"{meal_type}:\n"

            for added_product in sorted(sorted_product):
                result += f" - {added_product}\n"

        return result

    else:
        return "No products in the cart!"


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
