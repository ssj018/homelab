import myqueue

def hotPotatos(namelist, num):
    simqueue = myqueue.queue()
    for  i in  namelist:
        simqueue.enqueue(i)

    while simqueue.size()>1:
        for  i  in  range(num):
             simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()
    
    return simqueue.dequeue()

if __name__ == "__main__":
    namelist = [x+1 for  x  in range(39)]
    name = hotPotatos(namelist, 7)
    print(name)