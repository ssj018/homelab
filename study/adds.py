# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getNumFromList(self,l1):
        num = 0
        for i in range(len(l1)):
            num +=(l1.pop(0) * (10**i))
        return num
    
    def splitNumToList(self, num, numlist):
        numlist.append(num%10)
        if num//10 == 0:
            return 
        else:
            num = num //10
            self.splitNumToList(num, numlist)
    
    def translateListNodeToList(self, listnode, mylist):
        mylist.append(listnode.val)
        if listnode.next == None:
            return
        else:
            listnode = listnode.next
            self.translateListNodeToList(listnode, mylist)
    
    def translateListToListNode(self,mylist):
        listnode = ListNode(mylist.pop())
        while len(mylist)>0 :
            templistnode = listnode
            listnode = ListNode(mylist.pop())
            listnode.next = templistnode 
            
        return listnode

            
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1 = []
        self.translateListNodeToList(l1, list1)
        list2 = []
        self.translateListNodeToList(l2, list2)

        num1 = self.getNumFromList(list1)
        num2 = self.getNumFromList(list2)
        num = num1 + num2
        numlist = []
        self.splitNumToList(num, numlist)
        # print(numlist)
        return self.translateListToListNode(numlist)
        
if __name__ == "__main__":
    list1 = [2,3,4]
    list2 = [3,0,8]
    so = Solution()
    l1 = so.translateListToListNode(list1)
    l2 = so.translateListToListNode(list2)
    print(l1)
    # numlist = []
    # num = so.addTwoNumbers(l1,l2)
    # so.translateListNodeToList(num, numlist)
    # print(numlist)