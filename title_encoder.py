"""
PROBLEM:
- A file "books.txt" with book titles, each on a separate line
- Encode the title: "Game of Thrones" -> "GoT"

TASK:
- Read the file
- Encode each title
- Output the encoded version, each on a new line

WHAT TO DO:
- Read the file, get the content into a list of titles
- Loop through list of titles, split each title in a list of word
- Loop through the list of word and print a result string of first letters
"""

book_file = open("texts/books.txt")
content = book_file.readlines()

for line in content:
    # line is a list
    str = ""
    #loop through the list of words
    for word in line.split():
        str += word[0]
        
    print(str)
    
wrfile.close()   
        
        



