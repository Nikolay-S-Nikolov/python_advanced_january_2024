def cookbook(*args):
    recipes = {}

    for recipe_name, cuisine, ingredients in args:

        if cuisine not in recipes:
            recipes[cuisine] = []
        recipes[cuisine].append([recipe_name, ingredients])

    result = ''

    for cuisine_sorted, datta in sorted(recipes.items(), key=lambda x: (-len(x[1]), x[0])):
        result += f'{cuisine_sorted} cuisine contains {len(datta)} recipes:\n'
        for recipe_name, r_ingredients in sorted(datta):
            result += f'  * {recipe_name} -> Ingredients: {", ".join(r_ingredients)}\n'

    return result