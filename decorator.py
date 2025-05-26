#decorators in python is a special function that modifies the behavior of another function without changing its code. Decorators are often used to add extra functionality (like logging, timing, or access control) to existing functions in a clean and readable way.

def my_decorator(func):  #func refers to the original function
    def wrapper():
        print("Something is happening before the function is called.")
        func() #call the original function
        print("Something is happening after the function is called.")
    return wrapper

#say_whee = my_decorator(say_whee)
@my_decorator
def say_whee():
    print("Whee!")

say_whee()

#When wrapper() calls func(), it is calling the original say_whee() function.
#func is just a parameter name for the function being decorated.
#Now, say_whee actually refers to the wrapper function inside the decorator.
#my_decorator is called only once, when the function is defined (at decoration time).


def decorator1(fun): #fun=say_hello
    def wrapper(*args,**kwargs):
        print("SOMETHING BEFORE THE FUNCTION IS CALLED")
        fun(*args,**kwargs)
        print("SOMETHING AFTER THE FUNCTION IS CALLED")
    return wrapper

#say_hello = decorator1(say_hello)
@decorator1
def say_hello(x,y):
    print("hello",x,y)

say_hello("Ram","Shyam")

#with parameter function and parameter decorator

def great_decorator(greetings): #greetings="HELLO!!!"
    def decorator1(fun): #fun=say_hello
        def wrapper(*args,**kwargs):
            print("SOMETHING BEFORE THE FUNCTION IS CALLED")
            fun(*args,**kwargs)
            print(greetings)
        return wrapper
    return decorator1


@great_decorator("HELLO!!!")
def say_hello(x,y): #if say_hello(*args,**kwargs) then it can accept any no of argument
    print("ALICE AND HARRY",x,y)

say_hello("bob","Shelby")

import time 

def execution_time(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        result=func(*args,**kwargs)
        end_time = time.time()
        print(f"EXECUTION TIME OF {end_time-start_time} seconds")
        return result
    return wrapper

#example usage 
@execution_time
def example_function(n):
    total=0
    for i in range(n):
        total+=i

    return n

final_sum=example_function(100)
print("FINAL SUM IS",final_sum)

    

