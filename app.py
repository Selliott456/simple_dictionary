import json
from difflib import get_close_matches


data = json.load(open("data.json"))

def translate(word):
  word = word.lower()
  if word in data:
    return data[word]
  elif len(get_close_matches(word, data.keys())) > 0:
    yn =  input("did you mean %s? Enter Y or N:" % get_close_matches(word, data.keys())[0])
    if yn == "Y":
      return data[get_close_matches(word, data.keys())[0]]
    elif yn == "N":
      return "The word does not exist"
    else:
      return "That was not an option"
  else:
    return "The word doesn't exist"

user_word = input("Enter word: ")

output = (translate(user_word))

if type(output) == list:
  for item in output:
    print(item)
else:
  print(output)