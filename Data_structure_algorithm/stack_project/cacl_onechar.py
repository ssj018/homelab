import stack
import sys

def infixTopostfix(infixexpr):
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
        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYabcdefghijklmnopqrstuvwxyzZ0123456789':
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
    
    return ''.join(postfixlist)

def do_cacl(postfixexpr):
    datastack = stack.Stack()
    for  token in list(postfixexpr.replace(' ', '')):
        if token not in '+-*/0123456789':
            print('Wrong Exper')
            sys.exit(1)

        if token in '0123456789':
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
    print(newexpr.split())
    return newexpr.split()
    




if __name__ == "__main__":
    postfixlist1 = infixTopostfix('a + b*((c+d)*3-f/g)')
    postfixlist2 = infixTopostfix('31 + 60*((99+1876)*3-89076659/3983)')
    # print(postfixlist1)
    # print(postfixlist2)
   # print(do_cacl(postfixlist2))
    #print(do_cacl(postfixlist1))