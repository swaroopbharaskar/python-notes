year = int(input(“Enter a Year: “))
if year%4 == 0:
if year%100==0 and year%400 !=0:
    print(year,” is not a Leap Year”)
else:
    print(year,” is Leap Year”)
else:
    print(year,” is not a Leap Year”)