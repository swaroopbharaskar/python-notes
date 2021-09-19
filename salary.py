basic_pay=int(input("Enter basic pay : "))
hra=basic_pay*0.1
ta=(basic_pay*0.05)
total=basic_pay+hra+ta
pt=(basic_pay*0.02)
net_pay=total-pt
print("payable salary is:",net_pay)