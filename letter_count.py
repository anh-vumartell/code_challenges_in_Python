"""
Input: a string
Output: a dictionary of key is letter and value is each letter's count
- Get user input and store in variable named "string"
- Loop through input string, store each character as dictionary's key
- If a character repeats, increase the coresponding value of the key
- If a character is new, add new key to dictionary
"""
print("Please insert new word: ")
string = input()
dic = {}
for c in string:
    if c not in dic:
        dic[c] = 1
    elif c in dic:
        dic[c] += 1

print(dic)

            


