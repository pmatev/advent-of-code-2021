from typing import List, Tuple
from pprint import pprint
import re

def main():
    with open('13/input.txt', 'r') as f:  
        grid, folds = parse_input(f)
    
    # draw_grid(grid)

    for fold in folds:
        apply_fold(grid, fold)
        # draw_grid(grid)
        # print(count_grid(grid))
    
    draw_grid(grid)

def parse_input(file) -> Tuple[List[List[int]], List[Tuple[str, int]]]:
    points = []
    folds = []

    for line in file.readlines():
        cmd = line.rstrip()
        if not cmd:
            continue

        if cmd.startswith('fold'):
            match = re.match(r'fold along (x|y)=(\d+)', cmd)
            if match:
                folds.append(
                    (match[1], int(match[2]))  # e.g. (x, 4)
                )

        else:
            x, y = cmd.split(',')
            points.append((int(x), int(y)))
    
    grid_x = max(p[0] for p in points)
    grid_y = max(p[1] for p in points)
    dim = max(grid_x, grid_y) + 1

    grid: List[List[int]] = [
        [0 for i in range(dim)]
        for j in range(dim)
    ]

    for (x, y) in points:
        grid[y][x] = 1
    
    return grid, folds


def apply_fold(grid: List[List[int]], fold: Tuple[str, int]):
    # print('\n\n----', fold, '----\n\n')
    axis, fold_index = fold
    dim_x = len(grid)
    dim_y = len(grid[0])

    # draw the fold line
    if axis == 'x':
        for i in range(dim_x):
            grid[i][fold_index] = -1
    
    if axis == 'y':
        for i in range(dim_y):
            grid[fold_index][i] = -1

    # debug
    # draw_grid(grid)
    # print('\n')

    # do the fold
    if axis == 'x':
        for i in range(dim_x):        
            for j in range((dim_y // 2) + 1):
                grid[i][fold_index-j] = grid[i][fold_index+j] or grid[i][fold_index-j]
            
            # delete right of the fold
            grid[i][:] = grid[i][:fold_index]    
    
    if axis == 'y':
        for i in range(dim_y):
            # mirror values
            for j in range((dim_x // 2) + 1):
                grid[fold_index-j][i] = grid[fold_index+j][i] or grid[fold_index-j][i]
    
        # delete below the fold
        grid[:] = grid[:fold_index]

def draw_grid(grid: List[List[int]]):
    for i in grid:
        line = []
        for j in i:
            if j == 1:
                line.append('#')
            if j == 0:
                line.append('.')
            if j == -1:
                line.append('+')
        
        print(''.join(line))

def count_grid(grid: List[List[int]]):
    return sum(sum(y for y in x) for x in grid)  

if __name__ == '__main__':
    main()