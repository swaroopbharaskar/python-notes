n = int(input("enter the number : "))
s = 0
num = n
while(n>0):
    r = n%10
    s = s+(r**3)
    n = n/10
if(s==num):
    print("the number is armstrong")
else:
    print("the number is not armstrong")
