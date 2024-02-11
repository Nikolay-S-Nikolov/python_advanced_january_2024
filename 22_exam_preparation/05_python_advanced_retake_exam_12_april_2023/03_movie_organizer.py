def movie_organizer(*movie_and_genre):
    mary_collection = {}

    for movie, genre in movie_and_genre:

        if genre not in mary_collection:
            mary_collection[genre] = []

        mary_collection[genre].append(movie)

    result = ""

    for movie_genre, movies in sorted(mary_collection.items(), key=lambda x: (-len(x[1]), x[0])):
        result += f"{movie_genre} - {len(movies)}\n"
        for movie_name in sorted(movies):
            result += f"* {movie_name}\n"

    return result