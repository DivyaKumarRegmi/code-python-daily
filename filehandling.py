#FILE HANDLING
file=open('sample.txt', 'r') # open file in read mode


'''content=file.read() # read the content of the file
print(content) # print the content of the file
line1=file.readline()
line2=file.readline()
print(line1) # print the first line of the file
print(line2) # print the second line of the file'''

print(file.readlines()) # read all lines of the file and print them

file.close() # close the file

with open('sample.txt', 'r') as file: # open file in read mode and automatically close it after the block
    print(file.readlines()) # read all lines of the file and print them

with open("sample.txt",'r') as file:
    for line in file: # iterate through each line in the file
        print(line.strip()) # print each line

data=["new data1\nnew data2\nnew data3\n"] # list of new data to be written to the file
with open("newfile.txt",'w') as file: # open file in write mode
    file.write("this is a new file line 1\nthis is line 2 of new file\n") # write to the file
    file.write("this is line 3 of new file\n") # write to the file
    file.writelines(data) # write the list of new data to the file

with open("newfile.txt",'a') as file:
    file.write("appending new line 1\n") # append to the file






