# Initialize & Print: Create an array of size 5, assign values 1-5, and print them.
arr = [1, 2, 3, 4, 5]
print(arr)

# Sum of Elements: Iterate through an array and calculate the total sum.
sum1 = 0
for i in arr:
    sum1 += i
print(sum1)
print(sum(arr))

# Find Maximum: Iterate once to find the largest number.

max1 = float("-inf")
for i in arr:
    if i > max1:
        max1 = i

print(max1)
print(max(arr))

# Find Minimum: Iterate once to find the smallest number.
min1 = float("inf")
for i in arr:
    if i < min1:
        min1 = i
print(min1)
print(min(arr))

# Count Evens: Count how many numbers in the array are divisible by 2.
evens = 0
for i in arr:
    if i % 2 == 0:
        evens += 1
print(evens)
# Reverse Array (New Array): Create a new array that holds the elements in reverse order.
rev = []
for i in range(len(arr) - 1, -1, -1):
    rev.append(arr[i])

print(rev)
print(arr[-1])

# Reverse Array (In-Place): Reverse the array without creating a second one (swapping ends).
p, q = 0, len(arr) - 1
while p < q:
    arr[p], arr[q] = arr[q], arr[p]
    p += 1
    q -= 1
print(arr)

# Check if Sorted: Return true if array elements are in ascending order.
asc = True

for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        asc = False
        break
print(asc)

# Linear Search: Return the index of a specific number, or -1 if not found.

target = 4
for i in range(len(arr) - 1):
    if target == arr[i]:
        print(i)

# Copy Array: Manually copy all elements from Array A to Array B using a loop.
arr2 = []
for i in arr:
    arr2.append(i)

print(arr2)
