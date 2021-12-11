import sys
from typing import List, Tuple, Optional, Set
from termcolor import colored


def main():
    with open(sys.argv[1], 'r') as f:  
        input, boards = _parse_input(f)

    winners: List[Tuple[int, Board]] = []

    for i, num in enumerate(input):
        if len(winners) == len(boards):
            break

        for board in boards:
            if board in [b for _, b in winners]:
                continue

            board.mark(num)
            
            if board.complete():
                winners.append((num, board))
                continue

    num, board = winners[-1]
    print(num, board.sum_unmarked())
    print(num * board.sum_unmarked())


class Board:
    def __init__(self, cells: List[List[int]]) -> None:
        assert len(cells) == 5
        assert len(cells[0]) == 5
        self.cells = cells
        self.matched_cells: Set[Tuple[int, int]] = set()
        self.completed = False

    def __str__(self) -> str:
        return '\n'.join([
            ' '.join([self._print_cell(x, (i, j)) for j, x in enumerate(row)])
            for i, row in enumerate(self.cells)
        ])

    def _print_cell(self, cell, index) -> str:
        if index in self.matched_cells:
            if self.completed:
                return colored(f'{cell:02}', 'yellow')
            else:
                return colored(f'{cell:02}', 'green')
        else:
            return f'{cell:02}'
    
    def contains(self, value: int) -> Optional[Tuple[int, int]]:
        for i, row in enumerate(self.cells):
            for j, cell in enumerate(row):
                if cell == value:
                    return i, j
        return None
    
    def mark(self, value: int) -> None:
        match_idx = self.contains(value)
        
        if match_idx is not None:
            self.matched_cells.add(match_idx)

    def complete(self) -> bool:
        # check rows
        for row_idx in range(5):
            matched_row = len([(x, y) for (x, y) in self.matched_cells if x == row_idx]) == 5
            if matched_row:
                self.completed = True
                return True
        
        # check cols
        for col_idx in range(5):
            matched_col = len([(x, y) for (x, y) in self.matched_cells if y == col_idx]) == 5
            if matched_col:
                self.completed = True
                return True
        
        return False
    
    def sum_unmarked(self) -> int:
        total = 0
        for i, row in enumerate(self.cells):
            for j, cell in enumerate(row):
                if (i, j) not in self.matched_cells:
                    total += cell
        
        return total
        

def _parse_input(file) -> Tuple[List[int], List[Board]]:
    lines = [line.rstrip() for line in file.readlines()]
    input = [int(x) for x in lines[0].split(',')]
    boards = []

    for i in range(2, len(lines), 6):
        board = []
        for j in range(5):
            line = lines[i+j]
            board.append(_parse_board_line(line))
        
        boards.append(Board(board))

    return input, boards

def _parse_board_line(line: str) -> List[int]:
    values = []

    for i in range(0, len(line), 3):
        values.append(int(line[i:i+2]))
    
    return values
            

if __name__ == '__main__':
    main()