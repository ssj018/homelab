import sys
sys.path.append('/home/sunsj/vscode/homelab/calc_timer')
import calctimer

@calctimer.calctimes
def linear_search(li:list, val):
    for i in li:
        if i == val:
            return li.index(i)
    else:
        return None

@calctimer.calctimes
def binary_search(li, val):
    '''
    left: 第一个元素下标
    right: 最后一个元素下标
    mid: (left +right)/2 取整数部分
    如果mid>val, 证明待选区在mid的左边.
    right = mid -1
    如果mid<val, 证明待选区在mid右边.
    left = mid + 1
    '''
    left = 0
    right = len(li) - 1
    while left <= right: # 任然有待选区
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val:
            right = mid -1
        else:
            left = mid + 1
    else:
        return None

if __name__ == "__main__":
    li = list(range(1000000))
    linear_search(li, 39980)
    binary_search(li, 39980)