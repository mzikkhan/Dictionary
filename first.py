import json
from difflib import get_close_matches

data = json.load(open("C:\pythonbasics\App1\data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data: 
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0 :
        yn =  input("Did you mean %s instead? If yes, enter Y and if no, enter N: " % get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "Sorry, try again."
        else:
            return "Sorry please try again."
        
    else:
        return "Word does not exist. Please check again."

word = input('Enter word: ')

output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)