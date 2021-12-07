def main():
    increased = 0
    
    with open('input.txt', 'r') as f:  
        last = None
        cur = None

        for line in f:
            cur = int(line.strip('\n'))
            
            if last is None:
                last = cur

            if cur > last:
                increased += 1
            
            last = cur

    print('inc', increased)

if __name__ == '__main__':
    main()