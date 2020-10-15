import time

def calctimes(func):
    def innner(*args, **kwags):
        start = time.time()
        ret = func(*args, **kwags)
        end = time.time()
        used_time = end - start
        print('{} used {} seconds'.format(func.__name__, used_time))
        return ret
        
    return innner