qty = float(input("Enter the quantity of item sold :"))
val = float(input("Enter the value of item :"))
discount = float(input("Enter the  discount percentage :"))
tax = float(input("Enter the tax : "))
amt = qty * val 
discount_amt = (amt*discount)/100
sub_total = amt-discount_amt
tax_amt = (sub_total*tax)/100
total_amt = sub_total + tax_amt
print("*********BILL*********")
print("Quantity sold :  ",qty)
print("Price per item :  ",val)
print("Amount :  ",amt)
print("Discount :  ",discount_amt)
print("Discounted total :  ",sub_total)
print("Tax :  +",tax)
print("Total amount to be paid ",total_amt) 
print("Coded by Swaroop")