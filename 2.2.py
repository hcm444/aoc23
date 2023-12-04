games = []

with open("input.txt", "r") as file:
    input_data = file.read()

for line in input_data.splitlines():
    game_id_part, showings_part = line.split(': ')
    counts = {}
    for showing in showings_part.split('; '):
        for count, colour in (hint.split(' ') for hint in showing.split(', ')):
            count = int(count)

            if colour not in counts or count > counts[colour]:
                counts[colour] = count

    games.append({'id': int(game_id_part.replace('Game ', '')), 'max_counts': counts})

ps = sum(r * g * b for game in games
         for r, g, b in [(game['max_counts'].get('red', 0),
                                 game['max_counts'].get('green', 0),
                                 game['max_counts'].get('blue', 0))])

print(ps)
