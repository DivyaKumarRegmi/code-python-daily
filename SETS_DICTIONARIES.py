#SET
#unordered collection of unique elements
#mutable
#unindexed
#no duplicates
#unordered collection of unique elements
my_set = {1, 2, 3, 4, 5}
print(my_set)

my_set.add(6)#adds an item to the set
print(my_set)

my_set.remove(2)#removes the specified item
#raises an error if the item is not found
print(my_set)
my_set.discard(3)#removes the specified item
#does not raise an error if the item is not found
print(my_set)

myset= {1, 2, 5,4, 3}
print(myset)#automatically sorted in ascending order

#SET OPERATIONS
set1={1,2,3,4,5,6}
set2={6,7,8,9}

print(set1.union(set2))#returns a set that contains all items from both sets
print(set1|set2)#returns a set that contains all items from both sets

print(set1&set2)#returns a set that contains all items that exist in both sets  
print(set1.intersection(set2))#returns a set that contains all items that exist in both sets    

print(set1.difference(set2))#returns a set that contains all items from set1 except the items that are present in set2
print(set1-set2)#returns a set that contains all items from set1 except the items that are present in set2

print(set1^set2)#returns a set that contains all items that are present in only one of the sets
print(set1.symmetric_difference(set2))#returns a set that contains all items that are present in only one of the sets

print(set1.issubset(set2))#returns True if all items in set1 are present in set2
print(set1.issuperset(set2))#returns True if all items in set2 are present in set1

print(set1.isdisjoint(set2))#returns True if two sets have a null intersection
print(set1.clear())#removes all items from the set
print(set1)#returns an empty set

#FROZEN SETS
#immutable version of a set
fs=frozenset([1,2,3,4,5])
print(fs)#cannot be changed


#---------------------------------------------------------------------------------------------------
#DICTIONARY
#unordered collection of items
#mutable
#indexed by keys
#key-value pairs
#key must be unique
#values can be duplicated
#powerful and versatile data structure that allows you to store nd retrieve key value pairs
#similar to hash tables in other programming languages

user={
    'email':'123doe.com',
    'password':'123456',
    'address':'123 Main St',
}
print(user['email'])#accessing the value using the key
print(user.get('email'))#accessing the value using the get method
print(user.get('username'))#returns None if the key is not found
print(user.get('username','not found'))#returns the default value if the key is not found
print(user.keys())#returns a list of all the keys in the dictionary
print(user.get('address', 'BHAKTAPUR'))#returns the default value if the key is not found

print(user.values())#returns a list of all the values in the dictionary


user['email']='123bob.example.com.np'#updating the value of the key
user['username']='bob'#adding a new key-value pair to the dictionary
print(user)#returns the updated dictionary

print(user.pop('email'))#removes the specified key and returns the value
#del user['email']#removes the specified key and its value from the dictionary
print(user)#returns the updated dictionary

#DICTIONARY METHODS
# 1. clear() - Removes all items from the dictionary.
# 2. copy() - Returns a shallow copy of the dictionary.
# 3. len() - Returns the number of items in the dictionary.
# 4. items() - Returns a view object that displays a list of a dictionary's key-value tuple pairs.
# 5. keys() - Returns a view object that displays a list of all the keys in the dictionary.
# 6. values() - Returns a view object that displays a list of all the values in the dictionary.
# 7. get() - Returns the value of the specified key.
# 8. setdefault() - Returns the value of the specified key. If the key does not exist, insert the key with the specified value.
# 9. popitem() - Removes the last inserted key-value pair.
# 10. update() - Updates the dictionary with the specified key-value pairs.

#LOOP AND DICTIONARY COMPREHENSION
# Loop through a dictionary and print each key-value pair
for key, value in user.items(): 
    print(f"{key}: {value}")

    for i in user.values():# loop through the values in the dictionary
        print(i)
    for i in user.keys():# loop through the keys in the dictionary
        print(i)
    for i in user.items():# loop through the items in the dictionary
        print(i)

#DICTIONARY COMPREHENSION
# Dictionary comprehension is a concise way to create dictionaries in Python.
# It allows you to generate a new dictionary by applying an expression to each item in an existing iterable (like a list, tuple, or string).
# The syntax for dictionary comprehension is as follows:
# new_dict = {key: value for item in iterable if condition}
# Example: Create a dictionary with squares of numbers from 0 to 9
squares_dict = {x: x**2 for x in range(10)}
# print(squares_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

fruits = ["apple", "banana", "cherry"]

word_count = {word: len(word) for word in fruits}
print(word_count)  # Output: {'apple': 5, 'banana': 6, 'cherry': 6}

#NESTED DICTIONARY
# A nested dictionary is a dictionary that contains another dictionary as a value.
# It allows you to create complex data structures and organize related data in a hierarchical manner.

user = {
    'name': 'John Doe',
    'age': 30,
    'address': {
        'street': '123 Main St',
        'city': 'New York',
        'state': 'NY'
    },
    'hobbies': ['reading', 'traveling', 'cooking']
}
print(user['address']['city'])  # Output: New York
print(user['hobbies'][1])  # Output: traveling
print(user['address']['street'])  # Output: 123 Main St
print(user['address']['state'])  # Output: NY
print(user['hobbies'][0])  # Output: reading
print(user['hobbies'][2])  # Output: cooking
print(user['name'])  # Output: John Doe
print(user['age'])  # Output: 30
print(user['address'])  # Output: {'street': '123 Main St', 'city': 'New York', 'state': 'NY'}
print(user['hobbies'])  # Output: ['reading', 'traveling', 'cooking']
#print(user['address']['country'])  # Raises KeyError: 'country'

