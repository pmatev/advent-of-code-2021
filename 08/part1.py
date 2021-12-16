from collections import defaultdict
from typing import DefaultDict, List


def main():
    with open('08/input.txt', 'r') as f:  
        io_pairs = _parse_input(f)

        results: DefaultDict[int, int] = defaultdict(lambda: 0)

        for input_values, output_values in io_pairs:
            for v in output_values:
                if len(v) == 2:
                    results[1] += 1
                
                elif len(v) == 3:
                    results[7] += 1
                
                elif len(v) == 4:
                    results[4] += 1

                elif len(v) == 7:
                    results[8] += 1
        
        print(sum(results.values()))


def _parse_input(file):
    io_pairs = []

    lines = file.readlines()
    for line in lines:
        i, o = line.rstrip().split('|')
        
        io_pairs.append(
            (i.split(' '), o.split(' ')  )
        )
    
    return io_pairs

if __name__ == '__main__':
    main()