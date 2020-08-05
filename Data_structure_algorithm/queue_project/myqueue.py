
class queue:
    def __init__(self):
        self.mylist = []
    
    def isEmpty(self):
        return self.mylist == []
    
    def dequeue(self):
        return self.mylist.pop()
    
    def enqueue(self, item):
        self.mylist.insert(0, item)

    def size(self):
        return len(self.mylist)