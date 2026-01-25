import os
import sys
import time

# Count Vowels: Iterate a string and count 'a', 'e', 'i', 'o', 'u'.
v1 = ["a", "e", "i", "o", "u"]
v2 = "aeiou"
v3 = set("aeiou")
count, count2, count3 = 0, 0, 0

startime = time.perf_counter()
word = "Ramesh is here"
for i in word.lower():
    if i in v1:
        count += 1
print(count)
endtime = time.perf_counter()
print(endtime - startime)
print(sys.getsizeof(v1))


startime = time.perf_counter()
for i in word.lower():
    if i in v2:
        count2 += 1
print(count2)
endtime = time.perf_counter()
print(endtime - startime)
print(sys.getsizeof(v2))

startime = time.perf_counter()
count3 = sum(1 for i in word.lower() if i in v3)
print(count3)
endtime = time.perf_counter()
print(endtime - startime)
print(sys.getsizeof(v3))

# Reverse String: Create a new string that is the reverse of the input.
rev1, rev2 = "", ""
scentence = "Hello, i am ramesh vankdoth"
startime = time.perf_counter()
for i in range(len(scentence) - 1, -1, -1):
    rev1 += scentence[i]
print(rev1)
endtime = time.perf_counter()
print(f"{endtime - startime}")

startime = time.perf_counter()
rev2 = scentence[::-1]
print(rev2)
endtime = time.perf_counter()
print(endtime - startime)
# Check Palindrome: Check if string == reverse(string).

if scentence == rev1:
    print("Palindrome")
else:
    print("Not palindrome")

# Char to ASCII: Print the ASCII (integer) value of each character.
for i in scentence:
    print(ord(i))
# Remove Spaces: Create a new string with all spaces removed.

sc2 = "".join(scentence.split())
print(sc2.replace(",", ""))

# Count Occurrences: Count how many times the letter 'a' appears.
letter = "a"
countletter = 0
for i in scentence:
    if letter == i:
        countletter += 1

print(countletter)
print(sum(1 for i in scentence if i == letter))

# Toggle Case: Convert uppercase chars to lowercase and vice versa manually.
toggle = "I am Ramesh AnD I havE A VeRy keEN liKiNG tO coDinG worLRD"
ans = ""
print(toggle)
for i in toggle:
    if i.islower():
        ans += i.upper()
    else:
        ans += i.lower()
print(ans)
# Compare Strings: Write a function that returns true if two strings are identical (without using == or .equals).
# Method 1
st1 = "Ramesh"
st2 = "Ramesh"
equal = False
if len(st1) == len(st2):
    for i in range(len(st1)):
        if st1[i] != st2[i]:
            break
        equal = True
print(equal)

# Is Digit: Check if a string consists only of numbers "0" through "9".
cam = "323231276279264"
isdigit = False
d = "0123456789"
for i in cam:
    if i not in d:
        isdigit = False
        break
    isdigit = True

print(isdigit)
# Concatenate: Manually join two strings together into one new string.
concat = ""
concat = st1 + st2
print(concat)
