n = int(input("Enter : "))

for num in range(2,n) :
    p=True
    for i in range(2,num) :
        if (num%i==0) :
            p=False
    if p :
        print(num)
