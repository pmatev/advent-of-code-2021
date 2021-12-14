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
            # print('----', line)
            # pprint(grid)
        
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
    x_step = -1 if line.end[0] < line.start[0] else 1
    y_step = -1 if line.end[1] < line.start[1] else 1
    
    # horizontal
    if line.start[0] == line.end[0]:
        for y in range(line.start[1], line.end[1] + y_step, y_step):
            grid[y][line.start[0]] += 1
        
    # vertical
    elif line.start[1] == line.end[1]:
        for x in range(line.start[0], line.end[0] + x_step, x_step):
            grid[line.start[1]][x] += 1
    
    # diagonal
    else:
        xs = [x for x in range(line.start[0], line.end[0] + x_step, x_step)]
        ys = [y for y in range(line.start[1], line.end[1] + y_step, y_step)]
        for x, y in zip(xs, ys):
            grid[y][x] += 1
        
if __name__ == '__main__':
    main()