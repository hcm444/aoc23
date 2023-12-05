total=0
for i, arr in enumerate([list(line.strip()) for line in (open('1.txt').readlines())], start=1):
    if [int(j) for j in arr if j.isnumeric()]:
        result_str = str([int(j) for j in arr if j.isnumeric()][0]) + str([int(j) for j in arr if j.isnumeric()][-1])
        line = (int(result_str))
        total += line
print(total)
