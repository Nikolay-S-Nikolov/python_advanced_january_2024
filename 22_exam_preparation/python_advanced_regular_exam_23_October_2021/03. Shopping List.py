def shopping_list(budget: int, **kwargs):

    if budget < 100:
        return "You do not have enough budget."

    basket = 0
    result = []

    for product_name, price_quantity in kwargs.items():
        total_price = price_quantity[0] * price_quantity[1]

        if total_price <= budget:
            budget -= total_price
            result.append(f"You bought {product_name} for {total_price:.2f} leva.")

            basket += 1
            if basket == 5:
                break
    return '\n'.join(result)

