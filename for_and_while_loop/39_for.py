# 39. Count total words in a string using for loop.

s = input("Enter a string: ")
count = 0

for word in s.split():
    count += 1

print("Total words =", count)