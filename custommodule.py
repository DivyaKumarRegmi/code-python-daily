# creating custom module and importing functions as needed
import mymodule as mm 

result = mm.diff(10, 5)
print(result)

from mymodule import add , divide

from mymodule import add as a , divide as d

result = a(10, 5)
print(result)

result = d(10, 5)
print(result)

from mymodule import *#import all functions at once
result = add(2, 3)
print(result)

#list all the functions in the module
import mymodule
print(dir(mymodule))