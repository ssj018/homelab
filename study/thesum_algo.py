
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