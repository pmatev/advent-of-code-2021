import sys


class Submarine:
    def __init__(self) -> None:
        self.horiz = 0
        self.depth = 0

    def forward(self, distance):
        self.horiz += distance
    
    def up(self, distance):
        self.depth -= distance
    
    def down(self, distance):
        self.depth += distance


def main():  
    sub = Submarine()

    with open(sys.argv[1], 'r') as f:  
        for line in f:
            command, value = line.strip('\n').split(' ')
            distance = int(value)
            
            if command == 'forward':
                sub.forward(distance)
            
            elif command == 'up':
                sub.up(distance)
            
            elif command == 'down':
                sub.down(distance)

    print(sub.horiz * sub.depth)

if __name__ == '__main__':
    main()