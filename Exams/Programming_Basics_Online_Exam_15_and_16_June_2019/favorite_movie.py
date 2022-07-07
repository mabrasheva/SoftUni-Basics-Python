movie = input()
movies_count = 0
max_points = 0
best_movie = ""

while movie != "STOP":
    total_points = 0
    for character in movie:
        if 97 <= ord(character) <= 122:
            total_points += ord(character) - 2 * (len(movie))
        elif 65 <= ord(character) <= 90:
            total_points += ord(character) - len(movie)
        else:
            total_points += ord(character)

    if total_points > max_points:
        max_points = total_points
        best_movie = movie

    movies_count += 1
    if movies_count == 7:
        print(f"The limit is reached.")
        break

    movie = input()

print(f"The best movie for you is {best_movie} with {max_points} ASCII sum.")
