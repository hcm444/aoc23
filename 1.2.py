total = 0
alpha = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
for line in open("1.txt").read().strip().split('\n'):
    digits = []
    t_digits = []
    for i, j in enumerate(line):
        if j.isdigit():
            digits.append(j)
            t_digits.append(j)
        for k, val in enumerate(alpha):
            if line[i:].startswith(val):
                t_digits.append(str(k + 1))
    if digits:
        total += int(t_digits[0] + t_digits[-1])
print(total)
