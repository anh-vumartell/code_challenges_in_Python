text = input()
word = input()

def search_word(text, word):
    word_list = text.split(" ")
    if word in word_list:
        print("Word found")
    elif word not in word_list:   
        print("Word not found")

search_word(text, word)