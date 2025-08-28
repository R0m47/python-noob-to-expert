with open("Apprentice/level_19/Input/Letters/starting_letter.txt") as file:
    letter_content = file.read()

with open("Apprentice/level_19/Input/Names/invited_names.txt") as names:
    list_name = names.readlines()

for name in list_name:
    stripped_name = name.strip()
    new_letter = letter_content.replace("[name]", name)
    with open(
        f"Apprentice/level_19/Output/ReadyToSend/letter_for_{stripped_name}.txt",
        mode="w",
    ) as file:
        file.write(new_letter)
