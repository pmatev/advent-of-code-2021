import sys
from typing import List
from termcolor import colored


class Grid:
    def __init__(self, cells: List[List[int]]) -> None:
        self.cells = cells
        self.flashes = 0
    
    def __str__(self) -> str:
        return '\n'.join([
            ' '.join([colored(f'{cell}', 'white', attrs=['bold'] if cell == 0 else None) for cell in row])
            for row in self.cells
        ])
    
    def step(self) -> int:
        for i, row in enumerate(self.cells):
            for j in range(len(row)):
                self.cells[i][j] += 1

        self.flash(set())
        flash_count = len([cell for row in self.cells for cell in row if cell == 0])
        return flash_count
    
    @staticmethod
    def neighbors(i, j):
        return [
            (i+1, j),    # right-center
            (i-1, j),    # left-center
            (i, j+1),    # center-bottom
            (i, j-1),    # center-top
            (i+1, j+1),  # right-bottom
            (i-1, j+1),  # left-bottom
            (i+1, j-1),  # right-top
            (i-1, j-1),  # left-top
        ]
    
    def flash(self, flashed: set):
        # discharge all pending flashes
        update_needed = False

        for i, row in enumerate(self.cells):
            for j, cell in enumerate(row):
                if cell > 9:
                    # reset cell
                    self.cells[i][j] = 0
                    flashed.add((i, j)) 

                    # update neighbors
                    for (ni, nj) in self.neighbors(i, j):
                        if ni < 0 \
                            or ni >= len(self.cells) \
                            or nj < 0 \
                            or nj >= len(self.cells[0]):
                            continue

                        if (ni, nj) not in flashed:
                            self.cells[ni][nj] += 1

                        if self.cells[ni][nj] > 9:
                            update_needed = True
    
        if update_needed:
            self.flash(flashed)

def main():
    with open(sys.argv[1], 'r') as f:  
        grid = _parse_input(f)
    
    i = 0

    while i < 10000000:
        i += 1

        flash_count = grid.step()

        if flash_count == len(grid.cells) * len(grid.cells[0]):
            print(grid)
            print(i, flash_count)
            break


def _parse_input(file) -> Grid:
    lines = [l.strip() for l in file.readlines()]
    grid = []

    for line in lines:
        grid.append([int(v) for v in line])

    return Grid(grid)

if __name__ == '__main__':
    main()