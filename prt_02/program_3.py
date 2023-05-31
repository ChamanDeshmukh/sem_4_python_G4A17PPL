def union(lst_1,lst_2) :
    lst_3 = []
    lst_3 = set(lst_1+lst_2)
    lst_3 = list(lst_3)
    return lst_3    

def diff(lst_1,lst_2) :
    lst_3 = []
    lst_3 = list(set(list(set(lst_1)-set(lst_2)) + list(set(lst_2)-set(lst_1))))
    return lst_3    

#size = int(input("Enter Size of list : "))
#_list_ = []
#for e in range(size) :
#    _list_.append(input("Enter {}th : ".format(e+1)))
#
#
#size = int(input("Enter Size of list : "))
#_list2_ = []
#for e in range(size) :
#    _list2_.append(input("Enter {}th : ".format(e+1)))

_list_ = [1,2,3,4,5,8,8,0,1,6,7]
_list2_ = [1,2,3,4,5,6,7,8,0,4,1,6,9]

print(_list_)
print(_list2_)

print('Union : {}'.format(union(_list_,_list2_)))
print('Differance : {}'.format(diff(_list_,_list2_)))
