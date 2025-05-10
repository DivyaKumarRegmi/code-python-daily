t=(1,2,2,3,4,4,4)

print(t.count(2)) #gives how many time element is repeated
print(t.index(4)) #gives the index of first element

list=list(t)
print(list) #typecasting from tuple to list and reverse is also possible 

#tuple unpacking
colors=('red','green','blue')
r,g,b=colors
print(r,g,b)

#note:  list is dynamic but tuple are fixed so tuple is comparitively faster than list but we use list more than tuple
#because of its dynamic nature