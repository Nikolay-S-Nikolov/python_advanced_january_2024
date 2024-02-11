def forecast(*args):
    weather_dict = {"Sunny": 1, "Cloudy": 2, "Rainy": 3}
    condition_dict = {1: "Sunny", 2: "Cloudy", 3: "Rainy"}
    forecast_dict = {}

    for location, weather in args:
        forecast_dict[location] = weather_dict.get(weather)

    result = ''

    for city, condition in sorted(forecast_dict.items(), key=lambda x: (x[1], x[0])):
        result += f"{city} - {condition_dict[condition]}\n"

    return result