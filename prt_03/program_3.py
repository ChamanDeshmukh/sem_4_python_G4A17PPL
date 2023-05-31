import random

def __quick_sort__(lst, _left_, _right_):
    if _left_<_right_ :
        block = __partition__(lst, _left_, _right_) 
        __quick_sort__(lst, _left_, block - 1 ) 
        __quick_sort__(lst, block + 1, _right_)

def __partition__(lst, left, right):
    i = left
    j = right - 1
    pivot = lst[right]
    
    while i < j :
        while i < right and lst[i] < pivot : 
            i += 1
        while j > left and lst[j] >= pivot : 
            j -= 1
        if i < j:
            lst[i], lst[j] = lst[j], lst[i]
    if lst[i] > pivot:
        lst[i], lst[right] = lst[right], lst[i]
    
    return i
        
    
size = int(input("Enter Size : "))
_list_ = random.sample(range(100),size)
print("Before :",_list_)
__quick_sort__(_list_, 0, len(_list_)-1)
print("After : {}".format(_list_))
