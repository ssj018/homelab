class Stack:
    def __init__(self):
        self.mystack=[]
    
    def isEmpty(self):
        return self.mystack == []

    def peek(self):
        return self.mystack[len(self.mystack) - 1]

    def pop(self):
        return self.mystack.pop()
    
    def push(self, data):
        self.mystack.append(data)
    
    def size(self):
        return len(self.mystack)
    

if __name__ == "__main__":
    s = Stack()
    print(s.isEmpty())
    print(s.push(10))
    print(s.push('a'))
    print(s.peek())
    print(s.pop())
    print(s.size())