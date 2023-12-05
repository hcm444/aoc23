with open("2.txt", "r") as f:
    input_data = f.read()
max_r, max_g, max_b = 12, 13, 14
games = []
for line in input_data.splitlines():
    i, j = line.split(': ')
    counts = {}
    for k in j.split('; '):
        for x in k.split(', '):
            c, y = x.split()
            c = int(c)
            if y not in counts or c > counts[y]:
                counts[y] = c
    games.append({'id': int(i.replace('Game ', '')), 'counts': counts})
print(sum([g['id'] for g in (games) if
           g['counts'].get('red', 0) <= max_r and g['counts'].get('green', 0) <= max_g and
           g['counts'].get('blue', 0) <= max_b]))
