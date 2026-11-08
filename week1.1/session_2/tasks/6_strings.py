# For each of these string methods, run the code and work out what they do!
# add a comment using # to each one to explain what it does

user_string = input("Enter a string: ")

print(f"\nOriginal String: {user_string}") # enters it normally
print(f"Modified String 1: {user_string.lower()}") # lowercase word
print(f"Modified String 2: {user_string.upper()}") # uppercase word
print(f"Modified String 3: {user_string.strip()}") # removes spaces at the start and end
print(f"Modified String 4: {user_string.replace('a', '@')}") # replaces 'a' with '@'
print(f"Modified String 5: {user_string.capitalize()}") # uppercase first letter and lowercase the rest
print(f"Modified String 6: {user_string[::-1]}") # reverses the string
print(f"Modified String 7: {user_string.title()}") # uppercase first letter of each word
print(f"Modified String 8: {len(user_string)}") # number of characters in the string
print(f"Modified String 9: {user_string.find('a')}") # finds the position of 'a'
print(f"Modified String 10: {user_string.count('a')}") # counts how many a's there are
print(f"Modified String 11: {user_string.startswith('Hello')}") # checks if it starts with Hello 
print(f"Modified String 12: {user_string.endswith('!')}") # checks if it ends with !
print(f"Modified String 13: {user_string.isalnum()}") # checks if all characters are letters or numbers
print(f"Modified String 14: {user_string.isalpha()}") # checks if all characters are letters
print(f"Modified String 15: {user_string.isdigit()}") # checks if all characters are numbers



######
# if you finish, you can look at some more: https://www.w3schools.com/python/python_ref_string.asp
# and add some extras to this selection!
# You can also combine these functions - have a play around and see what you can do!