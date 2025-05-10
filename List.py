#list is a collection of items in a particular order
## mutable
# ordered
# indexed by position
# allows duplicates



#integer list
num = [1,2,3,4,5]

#indexing in list
print(num[0]) #outputs 1
print(num[1]) #outputs 2
print(num[-1]) #outputs 5

#slicing in list
print(num[1:4]) #outputs [2,3,4]
print(num[1:4:2])#outputs [2,4]
print(num[1:4:1])#outputs [2,3,4]
print(num[0:5:1])#outputs [1,2,3,4,5]
print(num[0:5:2])#outputs [1,3,5]
print(num[0:5:3])#outputs [1,4]


#appending new elements in list 
num.append(6)#adds 6 at the end of list
num.append(8)#adds 8 at the end of list
num.append(7)#adds 7 at the end of list
print(num) #outputs [1,2,3,4,5,6,8,7]
#popping elements from list 
num.pop(0)#removes 1 from the list
num.pop(1)#removes 3 from the list
num.pop(3)#removes 6 from the list
num.pop()#removes last element from the list

print(num)


#looping and conditionals,len()
num=[1,2,3,4,5]

for n in num:#looping through the list
    print(n)#outputs 1 2 3 4 5


#creating lists of lists 

matrix =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


print(matrix) #outputs whole matrix
print(matrix[0]) #outputs [1,2,3]
print(matrix[0][0]) #outputs 1
print(matrix[-1][1]) #outputs 8



#sum of all elements of all elements in a matrix: assignment
matrix =[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
total=0
for i in range(0,3):
    for j in range(0,3):
        total+=matrix[i][j]
print(f"Sum of all elements of given matrix is: {total}")


#print matrix in matrix format (assignment)

#membership operator in list
num=[1,2,3,4,5]
print(2 in num)
print(6 not in num)


#note : lists are mutable but tuples are not immutable

#list methods

#insert
colors=['red','green','blue']
colors.insert(1,'yellow')
colors.insert(0,'purple')
print(colors)
#note: append is more efficient than insert because it need to shift all items after it to insert which consumes more memory but append just add elements at the end 

#remove
colors.remove('purple')
print(colors)

#sort
print(sorted(colors)) #asscending order
print(sorted(colors,reverse=True)) #descending order 

#extend
more_colors=['black','white']
colors.extend(more_colors)
print(colors)

#list comprehension

#traditional way
sq=[]
for i in range(1,6):
    sq.append(i**2)
print(sq) #outputs [1,4,9,16,25]

#list comprehensive way
sq=[i**2 for i in range(1,6)]
print (sq) #outputs [1,4,9,16,25]

#can add condition as well:
sq=[i**2 for i in range(1,6) if i%2!=0]
print (sq) #outputs [1,9,25]
 

# create the filtering the even numbers
num=[1,2,3,4,5,6,7,8,9,10]
even_num=[n for n in num  if n%2==0]  #n in num extracts the elements while i in range gives the indexing
print(even_num)


#assignment: output [None,2,None,4,None,6,None,8] using list comprehension 
result = [None if i % 2 == 0 else i+1 for i in range(8)]
print(result)



sq=[]
sq=[i for i in range(8) if i%2==0]   #print even numbers upto 8 by list comprehension.
print(sq)


#matrix 
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for row in matrix:
    for col in row:
        print(col, end=" ")
    print("\n")