from random import randint

rock_paper_scissors = [
    """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""",
]

user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")
)

computer_choice = randint(0, 2)

print(rock_paper_scissors[user_choice])
print("Computer chose:")
print(rock_paper_scissors[computer_choice])

if user_choice >= 3 or user_choice <= 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 2 and computer_choice == 0:
    print("You lose!")
elif user_choice == computer_choice:
    print("Draw")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
