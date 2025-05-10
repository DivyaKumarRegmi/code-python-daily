# Integer Input and Operations
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum_result = num1 + num2
print("Sum of two numbers is", sum_result)
print(type(sum_result))

diff = num1 - num2
print("Difference of two numbers is", diff)
print(type(diff))

product = num1 * num2
print("Product of two numbers is", product)
print(type(product))

quotient = num1 / num2
print("Quotient of two numbers is", quotient)
print(type(quotient))

remainder = num1 % num2
print("Remainder of two numbers is", remainder)
print(type(remainder))


# Boolean Input and Operations
bool1 = bool(int(input("Enter first boolean (0 for False, 1 for True): ")))
bool2 = bool(int(input("Enter second boolean (0 for False, 1 for True): ")))

print("Boolean AND operation:", bool1 and bool2)
print("Boolean OR operation:", bool1 or bool2)
print("Boolean NOT operation on first boolean:", not bool1)
print("Type of boolean result:", type(bool1 and bool2))


# String Input and Operations
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

concat = str1 + str2
print("Concatenation of strings:", concat)
print("Type of concatenation result:", type(concat))

repeat3 = str1 * 3
print("Repeating first string 3 times:", repeat3)
print("Type of repeated string:", type(repeat3))

#comparison operators
print(num1>=num2)
print(num1<=num2)
print(num1==num2)
print(num1!=num2)
print(num1>num2)
print(num1<num2)
#strings are immutable
#single line string 'or" and multiline string"""
#each character in string is indexed
#also supports negative indexing

strng="hello! world"
strng="hi! there" #reassigning the string
print(strng[0]) 
print(strng[1])
print(strng[-1])
print(strng[-2])

#slicing is the process of extracting a substring from a string
print(strng[0:4]) #hi! t
print(strng[0:5:2]) #h!t
print(strng[0:5:1]) #hi! t
print(strng[::-1]) #ereht !ih (reversing the string)
print(len(strng)) #length of the string
print(strng[0:len(strng)]) #hi! there
#character is a single symbol in a string
#substring is a sequence of characters in a string
#string methods
#string methods are functions that can be applied to strings to perform various operations
newstr=strng.replace("there", "hi") #replace the substring "there" with "hi"
print(newstr) #hi! hi
print(newstr.lower()) #hi! hi
print(newstr.upper()) #HI! HI
print(newstr.title()) #Hi! Hi
print(newstr.lstrip()) #hi! hi (removes leading and trailing whitespace)
print(newstr.rstrip()) #hi! hi (removes leading and trailing whitespace)
print(newstr.strip()) #hi! hi (removes leading and trailing whitespace)
#9860036647
#isdigit() #checks if the string is a digit
#isupper() #checks if the string is in uppercase