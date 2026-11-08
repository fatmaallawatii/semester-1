# Week 1.3, Session 2: Word Counter

# We want to read in a text file, and calculate how many words are in it. 
# You can use any of the .txt files to test this - or even make your own.

# open and read the file
with open("story.txt", "r") as file:
    text = file.read() 

# calculate the number of words
words = text.split()  
wordcount = len(words)

# hint: you could use .split() to break up by spaces
# hint: watch out for empty lines that might give you empty strings

# display the wordcount
print(wordcount)
# Here are the word counts you should get:
# story.txt - 290
# story2.txt - 326
# glasses.txt - 210