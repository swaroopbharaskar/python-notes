num1 = int(input("Enter Num 1:"))
num2 = int(input("Enter Num 2:"))
num3 = int(input("Enter num 3 :"))
if (num1 >= num2) and (num1 >= num3):
 largest = num1
elif (num2 >= num1) and (num2 >= num3):
 greatest = num2
else:
 greatest = num3
print("The greatest number is",greatest )