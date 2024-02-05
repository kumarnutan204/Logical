print("Hello ")
num = (int)(input("Enter the number of values you want to print for the fibbonaci series"))

print(num)

def fibbonaci(num):
    a=0
    b=1
    
    if(num<0):
        print("Enter a positive number")

    if(num==0):
        print(0)
    
    if(num==1):
        print(1) 
    elif(num>1):
        count=2
        print(a)
        print(b)
        while(count!=num):
            c=a+b
            a=b
            b=c
            print(c)
            count+=1       
   
fibbonaci(num) 