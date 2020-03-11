import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    closematch = get_close_matches(w,data.keys(),cutoff=0.8) 
    if w.upper() in data:
        return data[w.upper()]
    elif w.title() in data:
        return data[w.title()]
    elif w in data:
        return data[w]
    elif len(closematch)>0:
        for i in range(0,len(closematch)):
            correction = input(( "Did you mean %s instead?" % closematch[i]))
            if correction.lower() == 'y':
                return data[closematch[i]]
                break
        else:
            return "Word not found in dictionary."
    else:
        return "Word not found in dictionary."

def output(meaning):
    num = 1
    if type(meaning) == str:
        print(meaning)
    elif type(meaning) == list:
        for item in meaning:
            print(str(num) + ") " + item)
            num = num + 1

output(translate(input("Enter a word:")))


