"""
PROBLEM: 
- Valid name input's length: > 3
- Input a string
- Raise an exception if name is invalid -> Print "Invalid Name"
- If name is valid -> Print "Account Created"

WHAT TO DO:
- Take an input string, assign to variable str
- If str's length < 3, raise exception, print "Invalid Name"
- Else print "Account Created"
"""
try:
    str = input()
    if len(str) > 3:
        print("Account Created")
    else: 
        raise Exception
except:
    print("Invalid Name")
