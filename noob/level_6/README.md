## Level 6: Hangman Game

In this project, you will develop the classic Hangman game. You will learn to manage game flow with loops, handle state (lives, guessed letters), validate repeated inputs, and display ASCII art stages for the hangman visual.

**How to run:**

1. Save this code in a file named `hangman_game.py`.
2. Make sure you have the following helper modules in the same folder:
   - `hangman_words.py` with the list `word_list`.
   - `hangman_art.py` with the variables `stages` and `logo`.
3. Open the terminal and navigate to the folder.
4. Run:

   ```bash
   python hangman_game.py
   ```

5. Guess letters until you complete the word or run out of lives.

**Learning objectives:**

- Import modules and manage inter-file dependencies.
- Use `while` loops to control game flow.
- Manage lists and strings to show player progress.
- Control state with variables (`lives`, `correct_letters`).
- Handle repeated and invalid inputs.
- Integrate ASCII art to represent hangman stages.
