s, c = 0, {}
with open("input.txt") as f:
    for i, l in enumerate(f):
        h = l.split(": ")[1].split("|")
        w = [int(n) for n in h[0].split()]
        p, wa = 0, 0
        for n in [int(num) for num in h[1].split()]:
            p = 1 if n in w and p == 0 else p * 2
            wa += 1 if n in w else 0
        s += p
        c[i] = wa
a = {card: 1 for card in c}
for card in a:
    for i in range(c[card]):
        a[card + i + 1] += a[card]
print(sum(a.values()))
