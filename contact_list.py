"""
- Input: a string
- Task: search name from a list of contacts/ a list of tuples (name: string, age: int)
- Output: a string "John is 31"
"""
#-------------------------
"""
Pseudo code
Get string input and assign to variable "name"
For each contact in contact list
    if contact at index 0 equals "name":
        print string contact at index 0 is contact at index 1
        stop the loop
    else: 
        print a string "Not found"
"""
contacts = [('James', 42), ('Amy', 24), ('John', 31), ('Amanda', 63), ('Bob', 18)]
print("Please give a name: ")
name = input()
for contact in contacts:
    if name in contact:
        print("{} is {}".format(name, contact[1]))
       