from typing import List

def main():
    with open('06/input.txt', 'r') as f:  
        values = _parse_input(f)

    for i in range(80):       
        current_batch = values.copy()

        for vi, v in enumerate(current_batch):
            values[vi] -= 1

            if v == 0:
                values[vi] = 6
                values.append(8)

    print(len(values))


def _parse_input(file) -> List[int]:
    line = file.readline()
    return [int(x) for x in line.split(',')]
        

if __name__ == '__main__':
    main()