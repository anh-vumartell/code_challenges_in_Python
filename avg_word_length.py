"""
Input: a string represent a sentence
Output: an float number
Steps:
    - Initiate  a variable to store the result of letter count (letter_count)
    - Get user input
    - Split the sentence by the space to get a list of words
    - Loop through the list of words and add length of each word to variable letter_count
    - Divide the letter_count with the length of the word list
    - Print the above result as a float to the console
"""
letter_count = 0
print("Please insert your sentence: ")
sentence = input()
word_list = sentence.split(" ")
for word in word_list:
    letter_count+=len(word)

print(letter_count/len(word_list))