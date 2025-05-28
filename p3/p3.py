#!/usr/bin/env python3

import sys
import re

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    with open(input_file, 'r') as f:
        data = f.read()

    pattern = re.compile(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)')
    total = 0

    for a, b in pattern.findall(data):
        total += int(a) * int(b)

    print(total)

if __name__ == "__main__":
    main()