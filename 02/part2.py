import sys


class Submarine:
    def __init__(self) -> None:
        self.horiz = 0
        self.depth = 0
        self.aim = 0

    def forward(self, value):
        self.horiz += value
        self.depth += self.aim * value
    
    def up(self, value):
        # self.depth -= value
        self.aim -= value
    
    def down(self, value):
        # self.depth += value
        self.aim += value
    
    def __str__(self):
        return f'd {self.depth}, h {self.horiz}, a: {self.aim}'


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
            
            print(line, sub)

    print(sub.horiz, sub.depth)
    print(sub.horiz * sub.depth)

if __name__ == '__main__':
    main()