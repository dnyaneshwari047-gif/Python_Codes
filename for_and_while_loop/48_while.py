# 48. Check whether a number is strong number.

num = int(input("Enter a number: "))
temp = num
total = 0

while temp > 0:
    digit = temp % 10
    fact = 1

    for i in range(1, digit + 1):
        fact *= i

    total += fact
    temp //= 10

if total == num and num >= 0:
    print("Strong number")
else:
    print("Not a Strong number")