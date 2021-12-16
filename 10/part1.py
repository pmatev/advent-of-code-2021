from typing import List, Optional, Tuple
from pprint import pprint
from collections import defaultdict

PAIRS = {
    '[': ']',
    '{': '}',
    '<': '>',
    '(': ')'
}
INVERSE = {v: k for k, v in PAIRS.items() }
POINTS = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

def main():
    with open('10/input.txt', 'r') as f:  
        lines = _parse_input(f)

    points = 0

    for line in lines:
        failed = check_line(line)
        if failed:
            points += POINTS[failed]

    print(points)

def check_line(line: List[str]) -> Optional[str]:
    stack = []
    
    for char in line:
        if char in PAIRS:
            stack.append(char)
        
        if char in INVERSE:
            if stack[-1] == INVERSE[char]:
                stack.pop()
            else:
                print(f'expected {stack[-1]}, but found {char} instead')
                return char
    
    if len(stack):
        # incomplete
        pass

    return None
        

def _parse_input(file) -> List[List[str]]:
    result: List[List[str]] = []

    for line in file.readlines():   
        parsed_line = []
        for char in line.rstrip():
            parsed_line.append(char)
        
        result.append(parsed_line)
    
    return result


if __name__ == '__main__':
    main()