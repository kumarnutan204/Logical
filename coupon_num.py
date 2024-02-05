import random as ra

def coupon(a,b,c):
    count=0
    lst=[]
    while(len(lst)<c):
        ran=ra.randint(a,b)
        count+=1
        if ran not in lst:
            lst.append(ran)
    print(lst)
    print(count)


coupon(10,20,7)