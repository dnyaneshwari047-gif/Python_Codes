#Mini Project 1 : Smart Electricity Bill Calculator

customer_name = input("Enter Customer Name : ").title()
units = float(input("Enter Total Unit Consumed:"))

service_charges = 150

if units < 100:
    eneergy_charges = units * 3
elif units <= 200:
    energy_charges = (100 * 3) + ((units-100)* 5)
else:
    energy_charges = (100 * 3) + ((100*5) + (units - 200 ) * 7)

final_bill = energy_charges + service_charges

print("***************ELECTRICITY BILL*******************")
print("----------------------------------------------------")
print("Customer Name:",customer_name)
print("Total units consumed are:",units)
print("Energy charges:",energy_charges)
print("Service charges:",service_charges)
print("Final Bill is:",final_bill)

if final_bill > 5000:
    print("Usage Message : High Usage Bill")
else:
    print("Usage Message : Normal Usage Bill")
    


