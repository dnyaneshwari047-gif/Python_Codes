# Mini Project 2 : Online Shopping Checkout

customer_name = input("Enter Customer Name:").title()
purchase_amount = float(input("Enter Purchase Amount:"))
customer_type = input("Enter customer type(Regular / Premium):")


if purchase_amount >= 5000:
    discount = purchase_amount * 20 /100
elif purchase_amount >= 3000 and purchase_amount < 5000:
        discount = purchase_amount * 10 /100
elif purchase_amount >1000 and purchase_amount < 3000:
          discount = purchase_amount * 5 /100
else:
       discount = 0

#additional discount for premium customers
if customer_type.lower() == "premium":
       discount = discount + (purchase_amount * 5 / 100)

discountable_amount = purchase_amount - discount

#free delivery

if discountable_amount >= 2000:
       delivery_fee = 0
else:
       delivery_fee = 100

#final pay bill
final_bill = discountable_amount + delivery_fee

print("**********************Shopping Checkout Bill*************************")
print("-----------------------------------------------------------------------")
print("Customer Name:",customer_name)
print("Discount Amount:",discountable_amount)
print("Delivery Charges:",delivery_fee)
print("Final Bill:",final_bill)
