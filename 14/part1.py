from typing import List, Optional, Tuple
from collections import Counter


def main():
    with open('14/input.txt', 'r') as f:  
        poly, rules = _parse_input(f)
        
    steps = 10

    for _ in range(steps):
        new_poly = poly.copy()
        count_inserts = 0
        
        for i, char in enumerate(poly):
            if i >= len(poly) - 1:
                continue

            window = poly[i:i+2]
            
            for match, insert in rules:
                if window == list(match):
                    new_poly.insert(i + 1 + count_inserts, insert)
                    count_inserts += 1

        poly = new_poly        

    counter = Counter(poly)
    most_common = counter.most_common()
    print(most_common[0][1] - most_common[-1][1])


def _parse_input(file) -> Tuple[List[str], List[Tuple[str, str]]]:
    start = list(file.readline().rstrip())
    sep = file.readline()

    steps = [
        line.rstrip().split(' -> ')
        for line in file.readlines()
    ]
    return start, steps
        

if __name__ == '__main__':
    main()