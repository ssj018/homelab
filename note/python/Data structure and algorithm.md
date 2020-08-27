### 图灵机

### 问题分类
- What
   - 树状分支判定
- Why
   - 有限的公式序列证明
- How
   - 算法和流程解决过程


### 计算复杂性: 研究问题本质，安装难易程度
- 冒泡排序（每次选择最小的，进行排序）， 比较的次数是： n<sup>2</sup>
- Bogo （洗一次牌，检查是否排好序列，没有就继续洗牌，直到排好序）， 比较的次数是： n*n!

### 算法： 研究问题在不同现实资源约束下的解决方案，致力找到效率最高的方案

### 不可计算问题： 基于有穷观点的能行方法，已经被证明不存在解决方案
- 停机问题
- 无理数： 几乎所有的无理数，都无法通过算法来确定其任意一位是什么。可计算的无理数很少（圆周率pi,自然对数的底e）

### 算法分析，主要比较算法的执行效率
- （1 ... n）求和sum函数实现:
```
import time

def sum_add(num):
    star_time = time.time()
    thesum = 0
    for  i  in  range(1, num+1):
        thesum += i
    end_time = time.time()
    total_time = end_time - star_time
    return thesum, total_time

def sum_gaosi(num):
    star_time = time.time()
    thesum = (num * (num + 1))/2
    end_time = time.time()
    total_time = end_time - star_time
    return int(thesum), total_time



if __name__ == "__main__":
    result_gaosi, time_gaosi = sum_gaosi(10000001)
    result_add, time_add = sum_add(10000001)
    print('sum_gaosi result: {} \t time: {}'.format(result_gaosi, time_gaosi))
    print('sum_add result: {} \t time: {}'.format(result_add, time_add))
```
**output:**
```
sum_gaosi result: 50000015000001         time: 2.6226043701171875e-06
sum_add result: 50000015000001   time: 0.5056314468383789
```

### 大O表示法
- 衡量算法复杂度方法：统计赋值语句的数量
```
def sum_add(num):
    thesum = 0                     ### 1次
    for  i  in  range(1, num+1):   ### n 次
        thesum += i

    return thesum
```
**T<sub>(n)</sub>= n + 1**

```
def sum_gaosi(num):
    thesum = (num * (num + 1))/2 ### 1 次

    return int(thesum)
```
**T<sub>(n)</sub>= 1**

- T(n) 起决定性主导的部分，叫做数量级函数，记作： O(f(n)), 其中f(n), 表示T(n)主导部分。这称为大O表示法。

**比如：**

T(n) = n+1
主导部分是n,所以运行时间数量级就是:
O(n)

T<sub>(n)</sub> = 5n <sup>2</sup> + 27n + 10005

O<sub>(n)</sub> = n<sup>2</sup>

- 很多时候出来规模，数据本身也会影响算法运行时间，比如排序（杂乱无章的数据，和已经有一定顺序的数据），算法运行时间有平均、最好、最差，一般以平均时间进行分析

- 常见的大O数量级函数
   - O<sub>(1)</sub>         --- 常数 
   - O<sub>log(n)</sub>      --- 对数
   - O<sub>(n)</sub>         --- 线性
   - O<sub>（n*log(n)）</sub>    --- 对数线性
   - O<sub>(n<sup>2</sup>)</sub> ---平方
   - O<sub>(n<sup>3</sup>)</sub> ---立方
   - O<sub>(2<sup>n</sup>)</sub> --- 指数

### Linear Structure ： 线性结构
- Stack
    - LIFO （Last In First Out），只在顶端加入和移除数据
    - 举例：浏览起后退按钮，word撤销操作按钮
    - code：
    ```
    **用list实现stack，list尾部作为Stack顶部**

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
    
    ```

- Queue
   - FIFO(First In Fist Out), 对尾进对首出
   - 举例： 进程排队，热土豆，打印机队列。**queue 可以用于进行仿真模拟**
   - code:
```

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
```

- Deque
   - 双端队列，可以从两端进行添加，删除。每次先进先出或先进后出的概念
   - 举例： 判定回文词
   - code：
```
class Deque:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def addFront(self, item):
        self.items.append(item)
    
    def removeFront(self):
        return self.items.pop()
    
    def addRear(self, item):
        self.items.insert(0, item)
    
    def removeRear(self):
        return self.items.pop(0)
```
- List
   - 单项向链表,每个元素定义位节点,节点有数据和Next属性 
   - 双向链表, 每个节点有: data,next,previous属性
   - 链表的访问是从head开始,按照next逐个访问,所以在添加节点,从头部添加是最快捷的方法
   - 无序链表,数据无序,直接插入头或者尾(最好是从head添加).
   - 有序链表需要在删除和添加时,进行排序
   - code
```
目前只是单向列表的一些功能实现.另外还需要增加双向链表的实现

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previos = None

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
    # 这是Node不含previou的实现方式. 如果node含有previous(即双向链表可以更简单一点),
        current = self.head
        previos = None
        found = False
        while not found:
            if current.getdata() == item:
                found = True
            else:
                previos = current
                current = current.getnext()
        
        if previos == None:
            self.head = current.getnext()
        else:
            previos.setnext(current.getnext())
    
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
        

```

以上4种线性结构，区别在于： 在不同的方向（顶端，底端，双向）进行数据的增加删除