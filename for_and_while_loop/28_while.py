# 28. Check whether a number is Armstrong.

num = int(input("Enter a number: "))
temp = num
total = 0
digits = len(str(num))

while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10

if total == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")