import stack

def do_baseConvert(decNumber, base):
    digits = '0123456789ABCDEF'
    remstack = stack.Stack()

    while decNumber > 0 :
        rem = decNumber % base
        #print(rem)
        #base 16 余数最大是15，作为index 从digits中取出相应的表示字符
        remstack.push(rem)
        decNumber = decNumber // base
        # print(decNumber)

    newstring = ''
    while not remstack.isEmpty():
        newstring += digits[remstack.pop()]
    
    return newstring

if __name__ == "__main__":
    print(do_baseConvert(200, 16))
