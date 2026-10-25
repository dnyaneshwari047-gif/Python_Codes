# 33. Print reverse of a string using for loop.

s = input("Enter a string: ")
rev = ""

for ch in s:
    rev = ch + rev

print("Reversed string =", rev)