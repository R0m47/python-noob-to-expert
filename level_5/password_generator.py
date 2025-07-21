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
password = ""

total_quantity_chars = chars_quantity + symbols_quantity + numbers_quantity

while total_quantity_chars > 0:
    char_type = random.randint(1, 3)
    if char_type == 1 and chars_quantity != 0:
        chars_quantity -= 1
        password = password + letters[random.randint(0, len(letters) - 1)]
    elif char_type == 2 and symbols_quantity != 0:
        symbols_quantity -= 1
        password = password + symbols[random.randint(0, len(symbols) - 1)]
    else:
        numbers_quantity -= 1
        password = password + numbers[random.randint(0, len(numbers) - 1)]
    total_quantity_chars -= 1

print(f"Your password is: {password}")
