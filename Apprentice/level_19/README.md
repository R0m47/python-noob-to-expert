## Level 19: Mail Merge Project

Automate personalized letters using a mail merge technique. The program reads a template letter and a list of invitee names, then generates a new letter for each person by replacing a placeholder with their name.

**How to run:**

1. Create the folder structure: `Apprentice/level_19/Input/Letters/starting_letter.txt` and `Apprentice/level_19/Input/Names/invited_names.txt`

2. In `starting_letter.txt`, include a placeholder `[name]` where each invitee’s name should go.

3. In `invited_names.txt`, write each invitee’s name on a new line.

4. Save the script as `mail_merge.py` inside `Apprentice/level_19/`.

5. Run:

   ```bash
   python mail_merge.py
   ```

6. The program will generate one text file per invitee inside `Output/ReadyToSend/`.

**Learning objectives:**

-Read from and write to text files using context managers (`with open`).
-Clean input data using `strip()`.
-Perform bulk text generation with string replacement.
-Organize project files into input/output directories.
