import json

# s1 = input("what is your word: ")

def isWord(word):
    with open("words_dictionary.json", "r") as file:
        words = json.load(file)
        if word in words:
            return True
        else: 
            return False