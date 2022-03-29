"""
PROBLEM:
- Input a string
- Output each letter of the string in reversed order
WHAT TO DO:
- Create a function named spell()
- Use recursion to refer to the spell() function
- Find the base case when the recursion stop: len(str) == 1, function return str
- Other cases evoke spell() with the string without the last letter (slice the last letter), return the last
character of sliced text:  txt[len(text)-1]
"""
def spell(txt):
    if len(txt) <= 1:
        print(txt)
    else:
        print(txt[len(txt)-1])
        spell(txt[:-1])
    
#print("Please insert a string:")
txt = input()
spell(txt)
