import difflib
import json

# converting the json file into a python obj(a dict)
with open("m_eng_dictionary.json") as data_dict:
    eng_dictionary = json.load(data_dict)


def define_term(phrase):

    # get a list of all the dictionary terms(keys)
    dictionary_keys = eng_dictionary.keys()

    # get the words that are a possible match to the user's search term using the difflib module
    closest_match = difflib.get_close_matches(phrase, dictionary_keys)

    # check if the key of the word given exists in the dictionary
    if eng_dictionary.get(phrase) is not None:
        if isinstance(eng_dictionary[phrase], list):
            message = "\n".join(eng_dictionary[phrase])
        else:
            message = eng_dictionary[phrase]

    # if the word is misspelt, check if there is a close match by checking the length of closest_match list
    elif len(closest_match) >= 1:
        # ask user to confirm if the closest_match word matches what they wanted
        confirm_word = input(f"Did you mean '{closest_match[0]}'? Please type [Y/y] if Yes or [N/n] if No:\t")

        # if yes, get the closest_match word definition and display it to user.
        if confirm_word.lower() == 'y':
            message = "\n".join(eng_dictionary[closest_match[0]])

        # if no, inform member the word they are looking for does not exist.
        elif confirm_word.lower() == 'n':
            message = "Sorry. The word cannot be found in my dictionary."

        # if they enter any other character apart from 'y/Y' or 'n/Y', inform them of an incorrect entry
        else:
            message = "Incorrect entry."

    # if the word is misspelt & there are no matches, inform user that the word does not exist.
    else:
        message = f"Sorry. The word '{phrase}' does not exist."

    return message


word = input("Enter your word:\t").lower()

print(define_term(word))

