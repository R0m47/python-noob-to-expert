import pandas as pd

df = pd.read_csv("Apprentice/level_21/nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}
user_input = input("Enter a word: ").upper()
nato_translate = [nato_dict[letter] for letter in user_input]
print(nato_translate)
