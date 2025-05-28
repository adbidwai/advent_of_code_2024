#! /usr/bin/env python3

def count_word_in_grid(grid, word):
    n_rows = len(grid)
    n_cols = len(grid[0]) if grid else 0
    directions = [
        (0, 1),   # right
        (1, 0),   # down
        (0, -1),  # left
        (-1, 0),  # up
        (1, 1),   # down-right
        (1, -1),  # down-left
        (-1, 1),  # up-right
        (-1, -1), # up-left
    ]
    count = 0
    for i in range(n_rows):
        for j in range(n_cols):
            for dx, dy in directions:
                match = True
                for k in range(len(word)):
                    x = i + k * dx
                    y = j + k * dy
                    if not (0 <= x < n_rows and 0 <= y < n_cols and grid[x][y] == word[k]):
                        match = False
                        break
                if match:
                    count += 1
    return count

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python count_xmas.py <input_file>")
        sys.exit(1)
    filepath = sys.argv[1]
    with open(filepath, 'r') as f:
        grid = [line.strip() for line in f if line.strip()]
    result = count_word_in_grid(grid, "XMAS")
    print(result)
