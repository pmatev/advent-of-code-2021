import sys
from typing import List


def decimal_from_bytes(bytes: List[int]):
    return int(''.join([str(x) for x in bytes]), 2)
        

def main():  
    with open(sys.argv[1], 'r') as f:  
        lines = [x.strip() for x in f.readlines()]
        
        counts = [0 for _ in lines[0]]

        for line in lines:
            for i, bit in enumerate(line):
                if bit == '1':
                    counts[i] += 1
        
        gamma = [0 for _ in lines[0]]

        for i, count in enumerate(counts):
            if count > len(lines) // 2:
                gamma[i] = 1
        
        gamma_int = decimal_from_bytes(gamma)
        # print('gamma', gamma, gamma_int)
        
        epsilon = [int(not x) for x in gamma]
        epsilon_int = decimal_from_bytes(epsilon)
        # print('epsilon', epsilon, epsilon_int)

        print(gamma_int * epsilon_int)
        
            
if __name__ == '__main__':
    main()