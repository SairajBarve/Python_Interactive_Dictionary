import json
from difflib import get_close_matches

with open('data.json', 'r') as data_source:
    data_json = json.load(data_source)

word = input("Enter the word: ")
if word in data_json:
    print('\n'.join(data_json[word]))
elif word.lower() in data_json:
    print('\n'.join(data_json[word.lower()]))
elif get_close_matches(word, data_json.keys(), cutoff=0.6):
    word = get_close_matches(word, data_json.keys(), cutoff=0.6)[0]
    choice = input("Did you mean %s instead (y/n)?" % word)
    if (choice == 'y') or (choice == 'Y'):
        print('\n'.join(data_json[word]))
    else:
        print('Word does not exist! Please try again')
else:
    print('Word does not exist! Please try again')

