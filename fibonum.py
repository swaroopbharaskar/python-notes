def Fibo(x):
    a=0
    b=1
    if x==1:
        print(1)
    elif x<=0:
        print("Please enter number greater than 0.")
    for i in range (2,x):
         c=a+b
         a=b
         b=c
         print(c, end=" ")
x=int(input("To get Fibonacci series of a number. \nEnter the number: "))
Fibo(x)