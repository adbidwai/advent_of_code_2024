#! /usr/bin/env python3

import sys

# Auxiliary function
def is_safe(levels):
    """
    True if levels is strictly inc or dec AND each adj delta is [1, 3]
    """
    if len(levels) < 2:
        return True
    
    diffs = [levels[i+1] - levels[i] for i in range(len(levels)-1)]

    if any(d == 0 or abs(d) > 3 for d in diffs):
        return False

    if all(d > 0 for d in diffs) or all(d < 0 for d in diffs):
        return True
    return False

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    safe_count = 0

    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            levels = list(map(int, line.split()))
            if is_safe(levels):
                safe_count += 1

    print(safe_count)

if __name__ == "__main__":
    main()