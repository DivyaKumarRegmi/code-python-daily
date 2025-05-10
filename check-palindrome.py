#CHECK PALINDROME 
# This program checks if a string or number is a palindrome or not
# A palindrome is a word, phrase, number, or other sequences of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

# Take input from the user
user_input = input("Enter a number or string: ")

# Reverse the input and compare with the original
if user_input == user_input[::-1]:
    print(f"'{user_input}' is a palindrome.")
else:
    print(f"'{user_input}' is not a palindrome.")
