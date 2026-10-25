# 34. Check whether a string is palindrome using for loop.

s = input("Enter a string: ")
rev = ""

for ch in s:
    rev = ch + rev

if s == rev:
    print("Palindrome string")
else:
    print("Not a palindrome string")