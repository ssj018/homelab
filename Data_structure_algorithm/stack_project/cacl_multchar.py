import stack
import sys
import parcheck

def infixTopostfix(infixexpr):
    if not  parcheck.parchecker(infixexpr):
        print('Wrong input: par not matches')
        sys.exit(1)

    prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1

    #tokenlist = infixexpr.split()
    #tokenlist = list(infixexpr.replace(' ',''))
    tokenlist = get_list(infixexpr)
  #  print(tokenlist)
    postfixlist = []
    opStack = stack.Stack()
    for token in tokenlist:
        # 不是操作符号，即为计算数据
        if token not in '+-*/()':
            postfixlist.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            toptoken = opStack.pop()
            while toptoken != '(':
                postfixlist.append(toptoken)
                toptoken = opStack.pop()
        else:
            while not opStack.isEmpty() and  prec[opStack.peek()] >= prec[token]:
                postfixlist.append(opStack.pop())
            opStack.push(token)
    
    while not opStack.isEmpty():
        postfixlist.append(opStack.pop())
    
    return ' '.join(postfixlist)

def do_cacl(postfixexpr):
    datastack = stack.Stack()
    for  token in postfixexpr.split():
        if token not  in '+-*/' and not token.isdigit():
            print('Wrong input: {} is not a  number !'.format(token))
            sys.exit(1)

        # 不是操作符号，即为计算数据
        if token not in '+-*/':
            datastack.push(int(token))
        else:
            op2=datastack.pop()
            op1=datastack.pop() # 顺序不能错，后出栈的是op1
            data = do_math(token, op1, op2)
            datastack.push(data)
    return datastack.pop()

def do_math(op, op1, op2):
    if op == '+':
        return op1 + op2
    elif op == '-':
        return op1 - op2
    elif op == '*':
        return op1 * op2
    elif op == '/':
        return op1/op2
    else:
        print('wrong op!')
        sys.exit(1)

def get_list(expr):
    newexpr = expr.replace(' ','')
    for  i  in '+-*/()':
        newexpr = newexpr.replace(i, ' {}{}{} '.format(' ', i, ' '))
    return newexpr.split()
    




if __name__ == "__main__":
    postfixlist1 = infixTopostfix('a + b*((c+d)*3-f/g)')
    postfixlist2 = infixTopostfix('31 + 60*((99+1876)*3-89076659/3983)')
    print(postfixlist1)
    print(postfixlist2)
    print(do_cacl(postfixlist2))
    print(do_cacl(postfixlist1))