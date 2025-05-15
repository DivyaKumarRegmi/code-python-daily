list=["apple" ,"banana" ,"cherry"]
print (list)
print(list[0])
print(list[1])
 #variable unpacking
a,b,c = list
print(a)
print(b)
print(c)    
print(list)
for index,i in enumerate(list):
    print(f"{'index':<25},{'value':<12}")
    print("-"*50)
    print(f"{index:<25},{i:<12}")


#FUNCTIONS
# A function is a block of code that only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.
# Functions are defined using the def keyword, followed by the function name and parentheses.
# The code inside the function is indented.
# Functions can take parameters, which are variables that are passed into the function when it is called.   

    def myfirst_function():
        print("MY FIRST EVER FUNCTION IN PYTHON")
myfirst_function()

def squared_no(number):
    print(number**2)

squared_no(50)

def sq_no(number,power):
    return number**power
print(sq_no(9,0.5))

unknown_tuple = (1,2,3,4,5)
def unknown_args(*args):
    print(args)

unknown_args(1, 2, 3, 4)
# Output: (1, 2, 3, 4)

print(sq_no(power=2,number=4))#output: 16

#parameters is the variable listed in function definition
#arguments is the value that is passed to the function when it is called
#keyword arguments are the arguments that are passed to the function by keyword
#default arguments are the arguments that are passed to the function by default

def greet(name):  # 'name' is a parameter
    print(f"Hello, {name}!")

greet("Alice")  # 'Alice' is an argument
# Output: Hello, Alice!

#return statement is used to send value back to caller 
#return statement is used to exit a function and go back to the caller

def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8

#you can assign default values to parameters. if no arguments is passed default value is used 
def greet(name="Guest"):
    print(f"Hello, {name}!")
greet()  # Output: Hello, Guest!
greet("Bob")  # Output: Hello, Bob!

#keyword arguments are used to pass arguments to a function by keyword
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet(age=25, name="Alice")  # Output: Hello, Alice! You are 25 years old.

#VARIABLE LENGTH ARGUMENTS
# *args is used to pass a variable number of non-keyword arguments to a function
# **kwargs is used to pass a variable number of keyword arguments to a function

#*args (NON-KEYWORD ARGUMENTS)
#collects additional positional arguments as a tuple
def unknown_args(*args):
    print(args)

unknown_args(1, 2, 3, 4) 
# Output: (1, 2, 3, 4)


#**kwargs (Keyword Arguments)
#Collects additional keyword arguments into a dictionary.
def unknown_kwargs(**kwargs):
    print(kwargs)

unknown_kwargs(name="Alice", age=25)
# Output: {'name': 'Alice', 'age': 25}

#You can unpack a list, tuple, or dictionary into arguments using * or **.

## The `non-keyword variable length arguments` in Python are represented by `*args` and are used to
# pass a variable number of non-keyword arguments to a function. When `*args` is used in a function
# definition, it collects additional positional arguments as a tuple. This allows the function to
# accept any number of positional arguments when it is called.

def add(a, b, c):
    return a + b + c

numbers = (1, 2, 3)
print(add(*numbers))  # Output: 6#unpacking a tuple
#unpacking a list
numbers = [4, 5, 6]
print(add(*numbers))  # Output: 15
# The `#keyword variable length arguments` section in the code is demonstrating the usage of
# `**kwargs` in Python functions.
#keyword variable length arguments
details = {"name": "Alice", "age": 25} 
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet(**details)#unpacking a dictionary
# Output: Hello, Alice! You are 25 years old.
print (details)



def get_stats(numbers):
    min_value = min(numbers)
    max_value = max(numbers)
    sum_value = sum(numbers)

    return min_value, max_value, sum_value
result=get_stats([1, 2, 3, 4, 5])
print(result)  # Output: (1, 5, 15)
# The `get_stats` function takes a list of numbers as input and returns the minimum value, maximum value, and sum of the numbers in the list.

min_value, max_value, sum_value = get_stats([1, 2, 3, 4, 5])#tuple unpacking
print(f"Min: {min_value}, Max: {max_value}, Sum: {sum_value}")
print(numbers)

def calculate_price(unit_price, qty=1,dis=0.1):
    price = unit_price * qty
    discount = price * dis
    total_price = price - dis
    return total_price
price=calculate_price(100, 2, 0.2)  
print(price)


