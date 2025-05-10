#LOOP THROUGH EACH CHARACTER IN A STRING
text = "hello"
for char in text:
    print(char)

#LOOP THROUGH EACH CHARACTER IN A STRING WITH INDEX
text = "hello"
for i in range(len(text)):
    print(f"Index {i}: {text[i]}")

#LOOP THROUGH WORDS IN A STRING
#use split() to split the string into words
text = "Python is amazing"
for word in text.split():
    print(word)

#LOOP THROUGH A STRING IN REVERSE
#using slicing to reverse the string
text = "hello"
for char in text[::-1]:
    print(char)
#using reversed() function
text = "hello"
for char in reversed(text):
    print(char)

#LOOP THROUGH A STRING WITH enumerate()
text = "hello"
for index, char in enumerate(text):
    print(f"Index {index}: {char}")

#NESTED LOOPS WITH STRINGS
#nested loops to find common characters in two strings
text1 = "abc"
text2 = "bcd"
for char1 in text1:
    for char2 in text2:
        if char1 == char2:
            print(f"Common character: {char1}")

