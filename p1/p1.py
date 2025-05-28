#!/usr/bin/env python3

import sys

# Auxiliary function
def total_distance(left_ids, right_ids):
    """
    Given two lists of integers, sort each and return the sum of absolute differences between corresponding elements.
    """
    left_sorted = sorted(left_ids)
    right_sorted = sorted(right_ids)
    return sum(abs(a - b) for a, b in zip(left_sorted, right_sorted))

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    left_ids = []
    right_ids = []

    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) != 2:
                print(f"Skipping invalid line: {line!r}", file=sys.stderr)
                continue
            l, r = map(int, parts)
            left_ids.append(l)
            right_ids.append(r)

    if len(left_ids) != len(right_ids):
        print("Error: mismatched number of left/right IDs", file=sys.stderr)
        sys.exit(1)

    result = total_distance(left_ids, right_ids)
    print(result)

if __name__ == "__main__":
    main()
