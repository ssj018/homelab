class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        # self.previos = None

    def getdata(self):
        return self.data
    
    def getnext(self):
        return self.next
    
    # 单向列表不需要previous
    # def getprevios(self):
    #     return self.previos
    
    def setnext(self, next):
        self.next = next
    
    def setprevios(self, previos):
        self.previos = previos


class mylist:
    def __init__(self):
        self.head = None

    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp
    
    def size(self):
        current_item = self.head
        count = 0
        while current_item != None:
            count += 1
            current_item = current_item.getnext()
        
        return count
    
    def search(self, item):
        current_item = self.head
        found = False
        while current_item != None and not found:
            if current_item.getdata() == item:
                found = True
            else:
                current_item = current_item.getnext()
        
        return found
    
    def remove(self, item):
    # 这是None不含previou的实现方式. 如果node含有previous(即双向链表可以更简单一点),
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getdata() == item:
                found = True
            else:
                previous = current
                current = current.getnext()
        
        if previous == None:
            self.head = current.getnext()
        else:
            previous.setnext(current.getnext())

    def pop(self):
        current = self.head
        found =  False
        previous = None
        theLast = None
        while not found:
            if current.getnext() == None:
                found = True
                theLast = current
                previous.setnext(None)
            else:
                previous = current
                current = current.getnext()
        
        return theLast.getdata()

    def append(self, item):
        temp = Node(item)
        current = self.head
        found =  False
        while not found:
            if current.getnext() == None:
                found = True
                current.setnext(temp)
            else:
                current = current.getnext()
        

        
