l=[1, 2, 3,]
even=[]
odd=[]
n=int(input("Enter the number of elements to enter: "))
for i in range(n):
    x=int(input("Enter number: "))
    l.append(x)
print(l)
for a in l:
    if(a%2==0):
        even.append(a)
        print(even)
    if(a%2==1):
        odd.append(a)
print("This is the list of even number: ", even)
print("This is the list of odd number: ", odd)