import random
from hangman_words import word_list
from hangman_art import stages, logo

chosen_word = random.choice(word_list)
placeholder = ""
display = ""
correct_letters = []
game_over = False
lives = 6

for space in range(len(chosen_word)):
    placeholder += "_"

print(logo)
print(placeholder)

while not game_over:
    print(
        f"****************************{lives}/6 LIVES LEFT****************************"
    )
    guess = input("Guess a letter: ").lower()
    if guess in correct_letters:
        print(f"You've already guessed {guess}")
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print("That letter is not in the word, try another one")
        if lives == 0:
            game_over = True
            print("You lose.")

    if "_" not in display:
        game_over = True
        print("You win.")

    print(stages[lives])
