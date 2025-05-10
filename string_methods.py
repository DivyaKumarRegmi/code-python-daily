# String Methods in Python
strng="hi! there"
print(strng.upper()) #HI! THERE
print(strng.title()) #Hi! There
print(strng.capitalize()) #Hi! there
print(strng.strip()) #hi! there (removes leading and trailing whitespace)
print(strng.lstrip()) #hi! there (removes leading whitespace)
print(strng.rstrip()) #hi! there (removes trailing whitespace)
print(strng.replace("there", "hi")) #hi! hi replace(old, new) (replace the substring "there" with "hi")
print(strng.split()) #['hi!', 'there'] (splits the string into a list of words)
#startswith(prefix)--->True if the string starts with the specified prefix, otherwise False
print(strng.startswith("hi")) #True
print(strng.startswith("there")) #False
#endswith(suffix)-->True if the string ends with the specified suffix, otherwise False
print(strng.endswith("there")) #True
print(strng.endswith("hi")) #False
#count(substring)-->returns the number of occurrences of the substring in the string
print(strng.count("hi")) #1
print(strng.count("there")) #1
#find(substring)-->returns the index of the first occurrence of the substring in the string, or -1 if not found
print(strng.find("hi")) #0
print(strng.find("there")) #3
print(strng.find("notfound")) #-1

#isspace()-->returns True if all characters in the string are whitespace, otherwise False
print(strng.isspace()) #False
#isalpha()-->returns True if all characters in the string are alphabetic, otherwise False
print(strng.isalpha()) #False
#isalnum()-->returns True if all characters in the string are alphanumeric, otherwise False     
print(strng.isalnum()) #False
#isnumeric()-->returns True if all characters in the string are numeric, otherwise False
print(strng.isnumeric()) #False
#isupper()-->returns True if all characters in the string are uppercase, otherwise False
print(strng.isupper()) #False
#islower()-->returns True if all characters in the string are lowercase, otherwise False
print(strng.islower()) #False
#istitle()-->returns True if the string is in title case, otherwise False
print(strng.istitle()) #False


