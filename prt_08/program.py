from time import sleep
from threading import Thread
import random

def partition(array, low, high):
 
    pivot = array[high]
 
    i = low - 1
 
    for j in range(low, high):
        if array[j] <= pivot:
 
            i = i + 1
 
            (array[i], array[j]) = (array[j], array[i])
 
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    return i + 1

def quickSort(array, low, high):
    if low < high:
 
        pi = partition(array, low, high)
 
        quickSort(array, low, pi - 1)
 
        quickSort(array, pi + 1, high)
 

def task():
    data = []
    for i in range(20):
            data.append(random.randint(1,20))
    print("Unsorted Array")
    print(data)
    
    size = len(data)
    
    quickSort(data, 0, size - 1)
    
    print('Sorted Array in Ascending Order:')
    print(data)
    

t1 = Thread(target=task)
t2 = Thread(target=task)

t1.start()
t2.start()
