from typing import Optional, Tuple, List
from pprint import pprint


def main():
    with open('09/input.txt', 'r') as f:  
        grid = _parse_input(f)

    low_points = []
    for i, row in enumerate(grid):
        for j, v in enumerate(row):
            neighbors = get_neighbors(grid, i, j)
            
            if v < min(neighbors):
                low_points.append({
                    'value': v,
                    'risk_level': v + 1,
                    'i': i,
                    'j': j
                })

    print(sum(p['risk_level'] for p in low_points))
            

def get_neighbors(grid: List[List[int]], i: int, j: int) -> List[int]:
    neighbors = []

    # up
    if i > 0:
        neighbors.append(grid[i-1][j])
    
    # down
    if i < len(grid)-1:
        neighbors.append(grid[i+1][j])
    
    # left
    if j > 0:
        neighbors.append(grid[i][j-1])
    
    # right
    if j < len(grid[0]) - 1:
        neighbors.append(grid[i][j+1])

    return neighbors


def _parse_input(file) -> List[List[int]]:
    grid = []
    for line in file.readlines():
        row = []
        for v in line.rstrip():
            row.append(int(v))
        
        grid.append(row)
    
    return grid


if __name__ == '__main__':
    main()