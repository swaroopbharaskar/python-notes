pps=int(input("Enter marks of the pps subject: "))
M2=int(input("Enter marks of the M2 subject: "))
phy=int(input("Enter marks of the Physics subject: "))
bee=int(input("Enter marks of the Bee subject: "))
grph=int(input("Enter marks of the Graphics subject: "))
total=(pps+M2+phy+bee+grph)
avg=float(total)/5
if pps<40 or M2<40 or phy<40 or bee<40 or grph<40:
    print("Fail")
elif(avg>=75):
    print("Grade: Distinction")
elif(avg>=60 and avg<75):
    print("Grade: First")
elif(avg>=50 and avg<60):
    print("Grade: Second")
elif(avg>=40 and avg<50):
    print("Grade: Third")
else:
    print("Grade: Fail")