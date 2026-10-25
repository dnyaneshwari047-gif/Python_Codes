# 44. Print alternate characters of a string.

s = input("Enter a string: ")

for i in range(0, len(s), 2):
    print(s[i], end="")