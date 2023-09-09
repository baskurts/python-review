# The Python dictionary is a collection of key value pairs.
# A dictionary can be created by placing a sequence of numbers
# with curly braces, seperated by a comma or by using the dict
# function. Values in a dictionary can be of any data type and 
# may be repeated. Keys can't be repeated and must be
# immutable. Dictionary keys are case sensitive, same name
# but different cases of a key will be treated distinctly.

# This line of code creates an empty dictionary.
nums = {}
print(nums)

# This line of code creates an empty dictionary that has
# 5 key values.
nums = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
print(nums)

# This line of code is creating the same dictionary
# using the dict function
nums = dict({1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'})
print(nums)

# These lines of code are accessing an element value in
# the dictionary by using its key
print(nums[1])
nums[4] = 'six'
print(nums)

# If an attempt is made ti access an element that does not
# exist in the dictionary, a KeyError will be thrown
# print(nums[6])

# The Python len function tells the number of elements in a dictionary.
print(len(nums))

# The line of code is creating a dictionary of mixed values.
mixed_values = {1: 1, 2: 'two', 3: 3, 4: 'four', 5: 5}
print(mixed_values)

# The line of code is creating a dictionary of mixed keys.
mixed_keys = {1: 1, 2: 'two', 3: 3, 4: 'four', 5: 5}
print(mixed_keys)

# A very handy way to step through the keys in a dictionary
# is by using a for loop.
for key in nums:
    print(key, end=" ")
print()

# This line of code is using a for loop to print out the values
# in a dicitonary.
for val in nums.values():
    print(val, end=" ")
print()

# These lines of code are using a for loop to print out the keys
# and values in a dictionary
for key, value in nums.items():
    print(key, value, end=" ")
print()

# A very handy way to step through the keys in a dictionary
# is by using a for loop.
i = 1
while (i <= len(nums)):
    print(nums[i], end=" ")
    i += 1
print()

# Python has inbuilt functions that may be used to manipulate
# dictionaries.

# The get function gets the value for a specified key.
print(nums.get(1))
print(nums)

# The pop funcion removes the key value for a specified key.
nums.pop(4)
print(nums, " - pop function")

# The popitem function removes the last key valeu from the dictionary.
nums.popitem()
print(nums, " - popitem function")

# The update function updates a value in a dictionary.
nums.update({3: 'python'})
print(nums, " - update function")

# The clear function removes all key values from a dictionary
nums.clear()
print(nums, " - clear function")

