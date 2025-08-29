## Level 20: U.S. States Guessing Game (Turtle + Pandas)

Build an interactive geography quiz that asks the player to name U.S. states. Each correct answer labels the state on a blank U.S. map. Typing Exit generates a `CSV` file with the states the player still needs to learn.

**How to run:**

1. Install pandas (once):

   ```bash
   pip install pandas
   ```

2. Ensure this folder structure:

   ```bash
   Apprentice/level_20/
    blank_states_img.gif
    50_states.csv
   ```

   The CSV must include columns: `state`, `x`, `y` (with coordinates for labeling).

3. Save the script as `us_states_game.py`.

4. Run:

   ```bash
   python us_states_game.py
   ```

5. Type state names. Enter `Exit` anytime to create `states_to_learn.csv` with remaining states.

**Learning objectives:**

-Use `turtle` for simple GUIs and on-screen text placement.
-Read and filter tabular data with `pandas`.
-Create derived datasets and export CSVs.
-Combine user input loops with data-driven rendering.
