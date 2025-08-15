from caesar_cipher_art import logo

alphabet = [
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
]
run_program = True


def caesar(original_text, shift_amount, type):
    output_text = ""
    if type == "decode":
        shift_amount *= -1
    for char in original_text:
        if char not in alphabet:
            output_text += char
        else:
            shifts = alphabet.index(char) + shift_amount
            shifts %= len(alphabet)
            output_text += alphabet[shifts]
    print(f"Here's the {type} result: {output_text}")


print(logo)
while run_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == "encode" or direction == "decode":
        caesar(original_text=text, shift_amount=shift, type=direction)
    else:
        print("That option doesn't exist, you've to type 'encode' or 'decode'")
    run_program = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n"
    ).lower()
    if run_program == "no":
        run_program = False
