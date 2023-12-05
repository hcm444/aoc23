class Number:
    def __init__(self):
        self.value = ''
        self.coords = []

    def is_adjacent_to(self, symbol):
        symbol_x = symbol.x
        symbol_y = symbol.y

        for x, y in self.coords:
            if abs(x - symbol_x) <= 1 and abs(y - symbol_y) <= 1:
                return True
        return False


class Symbol:
    def __init__(self, character, x, y):
        self.value = character
        self.x = x
        self.y = y


def input_parser(file_path='3.txt'):
    schematic = []

    with open(file_path, 'r') as file:
        for j, line in enumerate(file):
            schematic_row = []

            current_number = Number()
            for i, character in enumerate(line.strip()):
                if character.isdigit():
                    current_number.value += character
                    current_number.coords.append((i, j))
                else:
                    if current_number.value:
                        schematic_row.append(current_number)
                        current_number = Number()

                    if character != '.':
                        schematic_row.append(Symbol(character, i, j))

            if current_number.value:
                schematic_row.append(current_number)

            schematic.append(schematic_row)

    return schematic


def part2(schematic):
    schematic_length = len(schematic)
    gear_ratio_sum = 0

    for j, row in enumerate(schematic):
        min_j = max(0, j - 1)
        max_j = min(schematic_length, j + 1)
        adjacent_rows = schematic[min_j:max_j + 1]

        for item in row:
            if item.value == '*':
                adjacent_parts = []

                for adj_row in adjacent_rows:
                    for other_item in adj_row:
                        if isinstance(other_item, Number) and other_item.is_adjacent_to(item):
                            adjacent_parts.append(other_item)

                if len(adjacent_parts) == 2:
                    part1, part2 = adjacent_parts
                    gear_ratio = int(part1.value) * int(part2.value)
                    gear_ratio_sum += gear_ratio

    return gear_ratio_sum


if __name__ == "__main__":
    schematic = input_parser()
    result_part2 = part2(schematic)
    print(result_part2)
