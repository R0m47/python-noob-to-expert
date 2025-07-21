import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the Password Generator!")

chars_quantity = int(input("How many letters would you like in your password? "))
symbols_quantity = int(input("How many symbols would you like? "))
numbers_quantity = int(input("How many numbers would you like? "))

total_quantity_chars = chars_quantity + symbols_quantity + numbers_quantity
password_chars = (
    random.choices(letters, k=chars_quantity)
    + random.choices(symbols, k=symbols_quantity)
    + random.choices(numbers, k=numbers_quantity)
)
random.shuffle(password_chars)
password = "".join(password_chars)

print(f"Your password is: {password}")
