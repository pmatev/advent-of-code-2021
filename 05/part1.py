import sys
from typing import Tuple, List
from dataclasses import dataclass
from pprint import pprint


def main():
    with open('5/input.txt', 'r') as f:  
        lines = _parse_input(f)
        dim_x = max([max(l.start[0], l.end[0]) for l in lines])
        dim_y = max([max(l.start[1], l.end[1]) for l in lines])
        dim = max(dim_x, dim_y) + 1

        grid = [
            [0 for x in range(dim)]
            for y in range(dim)
        ]
        
        for line in lines:
            _apply_line(grid, line)
        
        print(len([y for x in grid for y in x if y >= 2]))


@dataclass
class Line:
    start: Tuple[int, int]
    end: Tuple[int, int]


def _parse_input(file) -> List[Line]:
    results: List[Line] = []

    for line in file.readlines():
        start, end = line.split(' -> ')
        x1, y1 = start.split(',')
        x2, y2 = end.split(',')

        results.append(
            Line(start=(int(x1), int(y1)), end=(int(x2), int(y2)))
        )
    
    return results

def _apply_line(grid: List[List[int]], line: Line):
    if line.start[0] == line.end[0]:
        step = -1 if line.end[1] < line.start[1] else 1

        for y in range(line.start[1], line.end[1] + step, step):
            grid[y][line.start[0]] += 1
        
    if line.start[1] == line.end[1]:
        step = -1 if line.end[0] < line.start[0] else 1

        for x in range(line.start[0], line.end[0] + step, step):
            grid[line.start[1]][x] += 1
        

if __name__ == '__main__':
    main()