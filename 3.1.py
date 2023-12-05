class Number:
    def __init__(self):
        self.value = ''
        self.coordinates = []

class Symbol:
    def __init__(self, char, x, y):
        self.value = char
        self.x, self.y = x, y


if __name__ == "__main__":
    grid = []
    with open('3.txt', 'r') as f:
        for j, line in enumerate(f):
            row = []
            current_number = None

            for i, char in enumerate(line.strip()):
                if char.isdigit():
                    if not current_number:
                        current_number = Number()
                    current_number.value += char
                    current_number.coordinates.append((i, j))
                else:
                    if current_number:
                        row.append(current_number)
                        current_number = None

                    if char != '.':
                        row.append(Symbol(char, i, j))

            if current_number:
                row.append(current_number)

            grid.append(row)
    input_grid = grid
    total = 0
    for j, row1 in enumerate(input_grid):
        min_j, max_j = max(0, j - 1), min(len(input_grid), j + 1)
        adjacent_rows = input_grid[min_j:max_j + 1]

        for item in row1:
            if isinstance(item, Symbol):
                si, sj = item.x, item.y
                total += sum(
                    int(number.value)
                    for adjacent_row in adjacent_rows
                    for number in adjacent_row
                    if isinstance(number, Number) and any(
                        abs(i1 - si) <= 1 and abs(j1 - sj) <= 1 for i1, j1 in number.coordinates)
                )
    result_part1 = total
    print(result_part1)
