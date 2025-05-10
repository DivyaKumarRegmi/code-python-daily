a=10
b=40
c=30 #integer
d=3.14 #float
isValid = True #boolean
user=None #null
num=1+2j #complex
#string
s="hello world!"
print(s[-1]) # outputs !, indexing gives characters from string
print(s[-2]) #outputs d
print(s[-3]) #outputs l
print(s[-4]) #outputs r
print(s[0]) #outputs h
print(s[1]) #outputs e
print(s[0:5]) # outputs hello, slicing gives substring from string
print(s[0:5:2]) #outputs hlo jumping 2 skipping 1 steps, slicing with skipping 2 steps
print(s[::-1]) #reversing string
#string methods
print (len(s)) #gives length of the string
newstr = s.replace("world","python") #cant change in same memory location but returns new string so needs to be stored in a new variable
print(newstr)
s2="  hello world    "
print(s2.strip())
s3="1234"
print(s3.isdigit())
print(type(num))

#format and F-string
fname="Diwash"
lname="Gauli"
print("My Name is "+fname+ " "+lname)
print("My name is {} {}".format(fname,lname)) #format
print(f"My name is {fname} {lname}") #F-string