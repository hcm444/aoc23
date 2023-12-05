s = 0
c = {}
with open("input.txt") as file:
    for i, line in enumerate(file):
        j = line.split(": ")[1].split("|")
        num2 = set(map(int, j[0].split()))
        p = sum(1 for num in map(int, j[1].split()) if num in num2)
        p = 2 ** p if p > 0 else 0
        s += p
        c[i] = sum(1 for num in map(int, j[1].split()) if num in num2)
print(s)
