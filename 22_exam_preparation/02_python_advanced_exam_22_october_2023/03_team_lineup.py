def team_lineup(*player_and_country):
    player_and_country_dict = {}
    for player, country in player_and_country:
        if country not in player_and_country_dict:
            player_and_country_dict[country] = []
        player_and_country_dict[country].append(player)
    result = ''
    for team, members in sorted(player_and_country_dict.items(), key=lambda x: (-len(x[1]), x[0])):
        result += team + ":\n"
        for member in members:
            result += f"  -{member}\n"
    return result
