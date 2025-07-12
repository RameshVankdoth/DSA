import sys  # Importing sys module to get the memory size of objects

# 1. Create an empty list
arr = []

# 2. Create a tuple with various types of elements (integers, string, list, etc.)
arr2 = (10, 20, 30, "hello", [1, 2, 3], 1, 2, 3)

# 3. Create an empty set
arr3 = set()

# 4. Create an empty dictionary (we'll add elements later)
arr4 = {}

# Display the initial state of each collection and their memory usage
print(f"Initial state:")
print(f"arr: {arr} and {type(arr)} and arr size is {sys.getsizeof(arr)}")
print(f"arr2: {arr2} and {type(arr2)} and arr size is {sys.getsizeof(arr2)}")
print(f"arr3: {arr3} and {type(arr3)} and arr size is {sys.getsizeof(arr3)}")
print(f"arr4: {arr4} and {type(arr4)} and arr size is {sys.getsizeof(arr4)}")
print("=" * 50)

# 5. Append elements to the empty list 'arr'
arr.append(10)  # Add integer 10 to the list
arr.append(15)  # Add integer 15 to the list
arr.append(20)  # Add integer 20 to the list
arr.append([1, 2, 3, 4, 5])  # Add a list inside the list

# 6. Add elements to the empty set 'arr3'
arr3.add(10)  # Add integer 10 to the set
arr3.add("Hello")  # Add string "Hello" to the set
arr3.add(20)  # Add integer 20 to the set
arr3.add("Hello+")  # Add string "Hello+" to the set

# 7. Add key-value pairs to the empty dictionary 'arr4'
arr4["name"] = "John"  # Add key 'name' with value 'John'
arr4["age"] = 25  # Add key 'age' with value 25
arr4["city"] = "New York"  # Add key 'city' with value 'New York'

# Display the state of each collection after modifications
print(f"After adding elements:")
print(f"arr2: {arr2} and {type(arr2)} and arr size is {sys.getsizeof(arr2)}")
print(f"arr: {arr} and {type(arr)} and arr size is {sys.getsizeof(arr)}")
print(f"arr3: {arr3} and {type(arr3)} and arr size is {sys.getsizeof(arr3)}")
print(f"arr4: {arr4} and {type(arr4)} and arr size is {sys.getsizeof(arr4)}")
print("=" * 50)

# 8. Append more elements to 'arr' (including duplicates)
arr.append(15)  # Add integer 15 again (duplicate)
arr.append(20)  # Add integer 20 again (duplicate)
arr.append(15)  # Add integer 15 again (duplicate)
arr.append(20)  # Add integer 20 again (duplicate)

# 9. Add more elements to 'arr3' (including duplicates)
arr3.add(10)  # Add integer 10 (duplicate)
arr3.add("Hello")  # Add string "Hello" (duplicate)
arr3.add(10)  # Add integer 10 (duplicate)
arr3.add("Hello")  # Add string "Hello" (duplicate)

# 10. Add more key-value pairs to the dictionary 'arr4'
arr4["country"] = "USA"  # Add key 'country' with value 'USA'
arr4["occupation"] = "Engineer"  # Add key 'occupation' with value 'Engineer'

# Display the final state of each collection and their memory usage
print(f"After adding more elements:")
print(f"arr2: {arr2} and {type(arr2)} and arr size is {sys.getsizeof(arr2)}")
print(f"arr: {arr} and {type(arr)} and arr size is {sys.getsizeof(arr)}")
print(f"arr3: {arr3} and {type(arr3)} and arr size is {sys.getsizeof(arr3)}")
print(f"arr4: {arr4} and {type(arr4)} and arr size is {sys.getsizeof(arr4)}")
print("=" * 50)
