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


def encrypt(text, shift):
    encrypt_text = ""
    for char in text:
        if char not in alphabet:
            encrypt_text += char
        else:
            if shift < len(alphabet):
                shifts = alphabet.index(char) + shift
                encrypt_text += alphabet[shifts]
            else:
                shifts = len(alphabet) - shift - 1
                encrypt_text += alphabet[shifts]

    print(f"Here's the encode result: {encrypt_text}")


def decrypt(text, shift):
    decrypt_text = ""
    for char in text:
        if char not in alphabet:
            decrypt_text += char
        else:
            if shift < len(alphabet):
                shifts = alphabet.index(char) - shift
                decrypt_text += alphabet[shifts]
            else:
                shifts = len(alphabet) + shift + 1
                decrypt_text += alphabet[shifts]

    print(f"Here's the decode result: {decrypt_text}")


print(logo)
while run_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("That option doesn't exist, you've to type 'encode' or 'decode'")
    run_program = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n"
    ).lower()
    if run_program == "no":
        run_program = False
