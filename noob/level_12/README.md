## Level 12: Higher Lower — Followers

In this level, you will create a version of the Higher Lower game where you must guess which celebrity/entity has more followers.

**How to run:**

1. Save this code in a file named `higher_lower.py`.
2. Make sure you have in the same folder:
   - `high_lower_game_art.py` with `logo` and `vs`.
   - `high_lower_game_data.py` with the list `data` (each element must have `name`, `description`, `country`, and `follower_count`).
3. Open the terminal and navigate to the file’s folder.
4. Run:

   ```bash
   python high_lower_game.py
   ```

5. Type A or B to guess who has more followers and accumulate points.

**Learning objectives:**

- Select random elements and avoid immediate repetitions.
- Encapsulate UI logic in functions (`game_screen`, `print_compare`).
- Control game state and score.
- Validate inputs and provide immediate feedback.
- Work with local modules for art and data.
