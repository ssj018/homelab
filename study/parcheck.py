import stack

def parchecker(symbolchars):
    s=stack.Stack()
    symbolcharsList = list(symbolchars)
    parmatch = False
    for i in symbolcharsList:
        if i not in '({[)}]':
            continue

        if i in '({[':
            s.push(i)
        elif i in ')}]':
            if s.isEmpty():
                return parmatch
            top = s.pop()
            if matches(top, i):
                parmatch = True
            else:
                parmatch = False
                return parmatch

    
    if parmatch and s.isEmpty():
        return parmatch
    else:
        return False 


def matches(symbol1, symbol2):
    openpars = '({['
    closepars = ')}]'
    return list(openpars).index(symbol1) == list(closepars).index(symbol2)

if __name__ == "__main__":
    print(parchecker('(ddd)123())'))
    print(parchecker('((]ddd())'))
    print(parchecker('(([dd])ffr())'))
    print(parchecker('(([)](ff))'))