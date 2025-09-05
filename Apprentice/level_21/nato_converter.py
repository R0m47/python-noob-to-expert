import pandas as pd


df = pd.read_csv("Apprentice/level_21/nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}


def generate_phonetic():
    user_input = input("Enter a word: ").upper()
    try:
        nato_translate = [nato_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(nato_translate)


generate_phonetic()
