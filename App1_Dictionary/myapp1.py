import json

dic = json.load(open("data.json"))

def define(word):
    word = word.lower()
    if word in dic:
        return dic[word]
    else: 
        return "That is not a valid word!"


print(define(input("Lets define a word of interest: ")))