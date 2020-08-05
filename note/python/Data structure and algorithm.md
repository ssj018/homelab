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
   - 举例： 进程排队，打印机队列
- Deque
- List

以上4种线性结构，区别在于： 在不同的方向（顶端，底端，双向）进行数据的增加删除