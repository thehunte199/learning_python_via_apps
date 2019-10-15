import json
from difflib import get_close_matches, SequenceMatcher

dic = json.load(open("data.json"))

def define(word):
    if (word[0].isupper()):
        if (word in dic):
            return dic[word]
            
    word = word.lower()
    if word in dic:
        return dic[word]
    else: 
        found = get_close_matches(word, dic)
        if  len(found) > 0 :
            user_input = input("Did you mean %s? Please enter Y for yes or N for no: " % found[0])
            if (user_input == "Y"):
                return dic[found[0]]
            elif (user_input == "N"):
                return "I'm sorry, that is not a valid word."
            else:
                return "That is not acceptable user input. Please try again."
        else:
            return "I'm sorry, that is not a valid word."

output = define(input("Lets define a word of interest: "))

if type(output) == list:
    for definition in output:
        print(definition)
else:
    print(output)