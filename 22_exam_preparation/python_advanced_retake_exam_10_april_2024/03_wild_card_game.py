def draw_cards(*args, **kwargs):
    result = []
    cards = {'monster': [], 'spell': []}
    if args:
        for arg in args:
            cards[arg[1]].append(arg[0])
    if kwargs:
        for k, v in kwargs.items():
            cards[v].append(k)

    if cards['monster']:
        result.append("Monster cards:")
        sorted_monstercards = sorted(cards['monster'], reverse=True)
        for card in sorted_monstercards:
            result.append(f"  ***{card}")
    if cards['spell']:
        result.append("Spell cards:")
        sorted_spellcards = sorted(cards['spell'])
        for card in sorted_spellcards:
            result.append(f"  $$${card}")
    return f'\n'.join(result)