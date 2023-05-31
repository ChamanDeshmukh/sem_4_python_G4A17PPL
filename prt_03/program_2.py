import random
def __merge_sort__(_list_):
    if len(_list_) > 1 :
        
        left_list = _list_[:len(_list_)//2]
        right_list = _list_[len(_list_)//2:]
        
        __merge_sort__(left_list)
        __merge_sort__(right_list)
        
        i = j = k = 0
            
        while i < len(left_list) and j < len(right_list):   
            if left_list[i] <  right_list[j] :
                _list_[k] = left_list[i]
                i+=1
            else : 
                _list_[k] = right_list[j]
                j+=1
            k+=1
        while i < len(left_list) :
            _list_[k] = left_list[i]
            i+=1
            k+=1
        while j < len(right_list) :
            _list_[k] = right_list[j]
            j+=1
            k+=1
                
size = int(input("Enter Size : "))
_list_ = random.sample(range(100),size)
print("Before :",_list_)
__merge_sort__(_list_)
print("After : {}".format(_list_))
