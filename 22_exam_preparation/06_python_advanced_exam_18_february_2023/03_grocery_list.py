def shop_from_grocery_list(budget: int, grocery_list: list, *product_and_price):
    purchased = []

    for product, price in product_and_price:

        if product in grocery_list and product not in purchased:

            if budget >= price:
                purchased.append(product)
                budget -= price
                grocery_list.remove(product)
            else:
                break

    if grocery_list:
        result = f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."

    else:
        result = f"Shopping is successful. Remaining budget: {budget:.2f}."

    return result