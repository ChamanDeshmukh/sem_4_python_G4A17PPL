a = int(input("Enter A : "))
b = int(input("Enter B : "))
print("Before : \nA : {} \nB : {}".format(a,b))

tmp = a
a = b
b = tmp

print("After: \nA : {} \nB : {}".format(a,b))
