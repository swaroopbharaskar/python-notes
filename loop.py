i=int(input("enter start number"))
n=int(input("enter end number"))
print("even numbers are:")
num=0
cnt=0
while (i<=n):
    num=num+1
    if i%2==0:
        print(i,end=' ')
        cnt=cnt+1
    i=i+1   
print("/n iterations",num)
print("/ncount of even numbers:" ,cnt)