# 24. Count vowels in a string.

s = input("Enter a string: ")
count = 0

for ch in s.lower():
    if ch in "aeiou":
        count += 1

print("Vowels =", count)