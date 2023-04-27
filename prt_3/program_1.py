import random

def __bubble_sort__(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i]<lst[j]:
                temp = lst[j]
                lst[j] = lst[i]
                lst[i] = temp
    return lst

_list_ = random.sample(range(100),10)
print("Before :",_list_)
print("After : ",__bubble_sort__(_list_))

