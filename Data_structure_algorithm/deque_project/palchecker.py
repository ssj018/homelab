import deque

def palcheck(symbolexpr):
    symdeque = deque.Deque()
    for i  in  symbolexpr:
        symdeque.addFront(i)
    

    while symdeque.size() > 1:
        first = symdeque.removeRear()
        last = symdeque.removeFront()
        print(' {} {} ' .format(first, last))
        if first != last:
            return False
    
    return True

if __name__ == "__main__":
    print(palcheck('radar'))
    print(palcheck('raddar'))
    print(palcheck('ra0d0ar'))
    print(palcheck('radarr'))
    print(palcheck('adar'))
