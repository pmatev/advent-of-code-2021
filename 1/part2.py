import sys

def main():
    increased = 0
    decreased = 0
    same = 0
    
    with open(sys.argv[1], 'r') as f:  
        window = []
        last = None
        cur = None

        for line in f:
            item = int(line.strip('\n'))
            window.append(item)
            
            if len(window) < 3:
                continue
            
            if len(window) > 3:
                window.pop(0)

            cur = sum(window)
            
            if last is None:
                last = cur
                continue

            if cur > last:
                increased += 1
            elif cur < last:
                decreased += 1
            else:
                same += 1
            
            last = cur


    print('inc', increased)
    print('dec', decreased)
    print('same', same)

if __name__ == '__main__':
    main()