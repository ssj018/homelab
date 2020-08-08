import myqueue
import random

class Tasks:
    def __init__(self, time):
        self.timeStamp = time
        self.pages = random.randrange(1, 21)

    def getPages(self):
        return self.pages
    
    def getStamp(self):
        return self.timeStamp
    
    def getwaitTime(self, currentTime):
        return currentTime - self.timeStamp



class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0
    
    def tick(self):
        if self.currentTask != None:
            self.timeRemaining -= 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def isbusy(self):
        if self.currentTask != None:
            return True
        else:
            return False
    
    def startPrint(self, newtask: Tasks):
        self.currentTask = newtask
        self.timeRemaining =  newtask.getPages()*60/self.pagerate


def newPrintTask():
    num = random.randrange(1, 181)
    if num == 180: #1-180之间的任意数都可以，概率是1/180
        # print(num)
        return True
    else:
        return False


def simulation(numseconds, pagPerMinute):
    labPrinter = Printer(pagPerMinute)
    printQueue = myqueue.queue()
    waitTimes = []

    for currentsecond in  range(numseconds):
        # print(currentsecond)

        if newPrintTask():
            task = Tasks(currentsecond)
            printQueue.enqueue(task)
        
        #printQueue 不为空，则不会打印新的任务，新的任务需要等待
        if  not labPrinter.isbusy() and not printQueue.isEmpty():
            newtask: Tasks = printQueue.dequeue()
            waitTimes.append(newtask.getwaitTime(currentsecond))
            labPrinter.startPrint(newtask)
            
        labPrinter.tick() # 每次循环，如果timeRemaining 不为空则减去1s

    averageWait =  sum(waitTimes)/len(waitTimes)
    print('average wait time: {} , {} tasks remaining'.format(averageWait, printQueue.size()))


if __name__ == "__main__":
    for  i in  range(10):
        simulation(3600, 5)