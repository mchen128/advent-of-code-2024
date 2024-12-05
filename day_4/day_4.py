# Part 1
def check_east(letter_grid, starting_row, starting_column):
    if letter_grid[starting_row][starting_column] == 'X' and \
       letter_grid[starting_row][starting_column + 1] == 'M' and \
       letter_grid[starting_row][starting_column + 2] == 'A' and \
       letter_grid[starting_row][starting_column + 3] == 'S':
        return True
    else:
        return False

def check_southeast(letter_grid, starting_row, starting_column):
    if letter_grid[starting_row][starting_column] == 'X' and \
       letter_grid[starting_row + 1][starting_column + 1] == 'M' and \
       letter_grid[starting_row + 2][starting_column + 2] == 'A' and \
       letter_grid[starting_row + 3][starting_column + 3] == 'S':
        return True
    else:
        return False

def check_south(letter_grid, starting_row, starting_column):
    if letter_grid[starting_row][starting_column] == 'X' and \
       letter_grid[starting_row + 1][starting_column] == 'M' and \
       letter_grid[starting_row + 2][starting_column] == 'A' and \
       letter_grid[starting_row + 3][starting_column] == 'S':
        return True
    else:
        return False

def check_southwest(letter_grid, starting_row, starting_column):
    if letter_grid[starting_row][starting_column] == 'X' and \
       letter_grid[starting_row + 1][starting_column - 1] == 'M' and \
       letter_grid[starting_row + 2][starting_column - 2] == 'A' and \
       letter_grid[starting_row + 3][starting_column - 3] == 'S':
        return True
    else:
        return False

def check_west(letter_grid, starting_row, starting_column):
    if letter_grid[starting_row][starting_column] == 'X' and \
       letter_grid[starting_row][starting_column - 1] == 'M' and \
       letter_grid[starting_row][starting_column - 2] == 'A' and \
       letter_grid[starting_row][starting_column - 3] == 'S':
        return True
    else:
        return False

def check_northwest(letter_grid, starting_row, starting_column):
    if letter_grid[starting_row][starting_column] == 'X' and \
       letter_grid[starting_row - 1][starting_column - 1] == 'M' and \
       letter_grid[starting_row - 2][starting_column - 2] == 'A' and \
       letter_grid[starting_row - 3][starting_column - 3] == 'S':
        return True
    else:
        return False

def check_north(letter_grid, starting_row, starting_column):
    if letter_grid[starting_row][starting_column] == 'X' and \
       letter_grid[starting_row - 1][starting_column] == 'M' and \
       letter_grid[starting_row - 2][starting_column] == 'A' and \
       letter_grid[starting_row - 3][starting_column] == 'S':
        return True
    else:
        return False

def check_northeast(letter_grid, starting_row, starting_column):
    if letter_grid[starting_row][starting_column] == 'X' and \
       letter_grid[starting_row - 1][starting_column + 1] == 'M' and \
       letter_grid[starting_row - 2][starting_column + 2] == 'A' and \
       letter_grid[starting_row - 3][starting_column + 3] == 'S':
        return True
    else:
        return False

file = open('day_4/day_4_input.txt', 'r')

word_search = []
for line in file:
    word_search.append(line.strip())

NUM_ROWS = len(word_search)
NUM_COLUMNS = len(word_search[0])

xmas_count = 0
for row_index in range(NUM_ROWS):
    for column_index in range(NUM_COLUMNS):
        # print(f'Row: {row_index}, Column: {column_index}, Letter: {word_search[row_index][column_index]}')
        if row_index < 3:
            if column_index < 3:
                if check_east(word_search, row_index, column_index):
                    xmas_count = xmas_count + 1
                if check_southeast(word_search, row_index, column_index):
                    xmas_count = xmas_count + 1
                if check_south(word_search, row_index, column_index):
                    xmas_count = xmas_count + 1
            elif column_index >= 3 and column_index < NUM_COLUMNS - 3:
                if check_east(word_search, row_index, column_index):
                    xmas_count = xmas_count + 1
                if check_southeast(word_search, row_index, column_index):
                    xmas_count = xmas_count + 1
                if check_south(word_search, row_index, column_index):
                    xmas_count = xmas_count + 1
                if check_southwest(word_search, row_index, column_index):
                    xmas_count = xmas_count + 1
                if check_west(word_search, row_index, column_index):
                    xmas_count = xmas_count + 1
            else:
                if check_south(word_search, row_index, column_index):
                    xmas_count = xmas_count + 1
                if check_southwest(word_search, row_index, column_index):
                    xmas_count = xmas_count + 1
                if check_west(word_search, row_index, column_index):
                    xmas_count = xmas_count + 1
        elif row_index >= 3 and row_index < NUM_ROWS - 3:
            if column_index < 3:
                if check_east(word_search, row_index, column_index):
                    xmas_count = xmas_count + 1
                if check_southeast(word_search, row_index, column_index):
                    xmas_count = xmas_count + 1
                if check_south(word_search, row_index, column_index):
                    xmas_count = xmas_count + 1
                if check_north(word_search, row_index, column_index):
                    xmas_count = xmas_count + 1
                if check_northeast(word_search, row_index, column_index):
                    xmas_count = xmas_count + 1
            elif column_index >= 3 and column_index < NUM_COLUMNS - 3:
                if check_east(word_search, row_index, column_index):
                    xmas_count = xmas_count + 1
                if check_southeast(word_search, row_index, column_index):
                    xmas_count = xmas_count + 1
                if check_south(word_search, row_index, column_index):
                    xmas_count = xmas_count + 1
                if check_southwest(word_search, row_index, column_index):
                    xmas_count = xmas_count + 1
                if check_west(word_search, row_index, column_index):
                    xmas_count = xmas_count + 1
                if check_northwest(word_search, row_index, column_index):
                    xmas_count = xmas_count + 1
                if check_north(word_search, row_index, column_index):
                    xmas_count = xmas_count + 1
                if check_northeast(word_search, row_index, column_index):
                    xmas_count = xmas_count + 1
            else:
                if check_south(word_search, row_index, column_index):
                    xmas_count = xmas_count + 1
                if check_southwest(word_search, row_index, column_index):
                    xmas_count = xmas_count + 1
                if check_west(word_search, row_index, column_index):
                    xmas_count = xmas_count + 1
                if check_northwest(word_search, row_index, column_index):
                    xmas_count = xmas_count + 1
                if check_north(word_search, row_index, column_index):
                    xmas_count = xmas_count + 1
        else:
            if column_index < 3:
                if check_east(word_search, row_index, column_index):
                    xmas_count = xmas_count + 1
                if check_north(word_search, row_index, column_index):
                    xmas_count = xmas_count + 1
                if check_northeast(word_search, row_index, column_index):
                    xmas_count = xmas_count + 1
            elif column_index >= 3 and column_index < NUM_COLUMNS - 3:
                if check_east(word_search, row_index, column_index):
                    xmas_count = xmas_count + 1
                if check_west(word_search, row_index, column_index):
                    xmas_count = xmas_count + 1
                if check_northwest(word_search, row_index, column_index):
                    xmas_count = xmas_count + 1
                if check_north(word_search, row_index, column_index):
                    xmas_count = xmas_count + 1
                if check_northeast(word_search, row_index, column_index):
                    xmas_count = xmas_count + 1
            else:
                if check_west(word_search, row_index, column_index):
                    xmas_count = xmas_count + 1
                if check_northwest(word_search, row_index, column_index):
                    xmas_count = xmas_count + 1
                if check_north(word_search, row_index, column_index):
                    xmas_count = xmas_count + 1

print(f'Day 4, Part 1: {xmas_count}')

# Part 2
def check_cross_mas(letter_grid, row, column):
    if letter_grid[row][column] == 'A':
        if check_config_1(letter_grid, row, column) or \
           check_config_2(letter_grid, row, column) or \
           check_config_3(letter_grid, row, column) or \
           check_config_4(letter_grid, row, column):
            return True
    return False

def check_config_1(letter_grid, row, column):
    if letter_grid[row - 1][column - 1] == 'M' and \
       letter_grid[row - 1][column + 1] == 'M' and \
       letter_grid[row + 1][column + 1] == 'S' and \
       letter_grid[row + 1][column - 1] == 'S':
        return True
    return False

def check_config_2(letter_grid, row, column):
    if letter_grid[row - 1][column - 1] == 'S' and \
       letter_grid[row - 1][column + 1] == 'M' and \
       letter_grid[row + 1][column + 1] == 'M' and \
       letter_grid[row + 1][column - 1] == 'S':
        return True
    return False

def check_config_3(letter_grid, row, column):
    if letter_grid[row - 1][column - 1] == 'S' and \
       letter_grid[row - 1][column + 1] == 'S' and \
       letter_grid[row + 1][column + 1] == 'M' and \
       letter_grid[row + 1][column - 1] == 'M':
        return True
    return False

def check_config_4(letter_grid, row, column):
    if letter_grid[row - 1][column - 1] == 'M' and \
       letter_grid[row - 1][column + 1] == 'S' and \
       letter_grid[row + 1][column + 1] == 'S' and \
       letter_grid[row + 1][column - 1] == 'M':
        return True

xmas_count = 0
for row_index in range(NUM_ROWS):
    for column_index in range(NUM_COLUMNS):
        if row_index != 0 and row_index != NUM_ROWS - 1 and column_index != 0 and column_index != NUM_COLUMNS - 1:
            if check_cross_mas(word_search, row_index, column_index):
                xmas_count = xmas_count + 1
print(f'Day 4, Part 2: {xmas_count}')