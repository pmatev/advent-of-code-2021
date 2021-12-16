from typing import List


def main():
    with open('07/input.txt', 'r') as f:  
        values = _parse_input(f)
    
    median = sorted(values)[len(values) // 2]

    diff_to_median = [
        abs(v - median)
        for v in values    
    ]
    print(sum(diff_to_median))



def _parse_input(file) -> List[int]:
    line = file.readline()
    return [int(x) for x in line.split(',')]
        

if __name__ == '__main__':
    main()