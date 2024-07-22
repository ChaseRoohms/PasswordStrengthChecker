import re
import sys


from_leet_speak = {'4': 'a', '8': 'b', '3': 'e', '9': 'g', '1': 'l', '0': 'o', '5': 's', '7': 't', '2': 'z'}
lower_letter = r'.*[a-z].*'
upper_letter = r'.*[A-Z].*'
number = r'.*[0-9].*'
special_character = r'.*[~`!@#$%^&*()_\-+={[}\]\|\\:;"\'<,>\.?\/].*'


warnings = False


# Coloring / formatting of text
class Format:
    BLUE = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Loads a set with values from a text file
def load_set(filename):
    loaded_set = set()
    with open(filename, 'r', encoding="utf8") as file:
        for line in file.readlines():
            loaded_set.add(line.strip())
    return loaded_set


# Translates common "leet speak" characters to letters
def leet_checker(password):
    listed_password = list(password)
    for i, letter in enumerate(listed_password):
        if letter in from_leet_speak:
            listed_password[i] = from_leet_speak[letter]
    return "".join(listed_password)


# Checks if password matches some basic requirements
# REQUIRED: Contains an upper and a lowercase letter
# REQUIRED: Contains a number
# REQUIRED: Contains a special character
# REQUIRED: Length >= 8
# SUGGESTED: Length >= 12
def check_requirements(password):
    global warnings
    if not re.match(lower_letter, password):
        print(Format.FAIL + "Password is missing a lowercase letter" + Format.END)
        quit()
    elif not re.match(upper_letter, password):
        print(Format.FAIL + "Password is missing an uppercase letter" + Format.END)
        quit()
    elif not re.match(number, password):
        print(Format.FAIL + "Password is missing a number" + Format.END)
        quit()
    elif not re.match(special_character, password):
        print(Format.FAIL + "Password is missing a special character" + Format.END)
        quit()
    elif len(password) < 8:
        print(Format.FAIL + "Password must be at least 8 characters" + Format.END)
        quit()
    elif len(password) < 12:
        warnings = True
        print(Format.WARNING + "Suggested password length is 12 characters or more" + Format.END)


# Checks for dictionary words in a password
def dict_checker(password):
    global warnings
    dictionary = load_set("word_sets/dictionary.txt")
    checked_for_leet_password = leet_checker(password)
    dict_words_in_password = list()

    for word in dictionary:  # Check if any dictionary word is in the password, or in its leet version
        word = word.lower()
        if len(word) >= 4 and (word in password.lower() or word in checked_for_leet_password.lower()):
            dict_words_in_password.append(word)
            warnings = True
            print(Format.WARNING + "Your password may contain a dictionary word" + Format.END)
            break


# Checks if password is one of the 1m most common passwords
def commonality_checker(password):
    if password in load_set("word_sets/1m_common_password.txt"):
        print(Format.FAIL + "Your password is one of the 1 million most common passwords" + Format.END)
        quit()


# MAIN PROGRAM
if len(sys.argv) != 2:
    print(Format.FAIL + "Usage: password_strength.py <password>" + Format.END)
    quit()
else:
    user_password = sys.argv[1]
    check_requirements(user_password)       # Checks length, and contents against basic requirements
    commonality_checker(user_password)      # Checks if password is one of the 1 million most common passwords
    dict_checker(user_password)             # Checks if password contains dictionary words

    print()
    if warnings:
        print(Format.BOLD + Format.BLUE + "Your password is usable, but can be improved. Check the warnings above for "
                                          "more information." + Format.END)
    else:
        print(
            Format.BOLD + Format.BLUE + "Your password is usable and very strong!" + Format.END)