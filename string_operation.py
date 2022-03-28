"""
-Input: string
-Output: string, input string's character repeated N times. N = character's index
Pseudo code
- Get input
- Loop through the string with number of loops = length of str
- Starting i = 1
"""
str = input()
i = 1
while i <= len(str):
    for c in str:
        print(c*i)
        i+=1
   

