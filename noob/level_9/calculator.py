from calculator_art import logo
import os


def add(first_number, second_number):
    return first_number + second_number


def substract(first_number, second_number):
    return first_number - second_number


def multiply(first_number, second_number):
    return first_number * second_number


def divide(first_number, second_number):
    return first_number / second_number


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}


def calculate_result(sign, first_number, second_number):
    result = operations[sign](first_number, second_number)
    print(f"{first_number} {sign} {second_number} = {result}")
    return result


def calculator():
    print(logo)
    continue_calculation = True
    first_number = 0
    second_number = 0
    while continue_calculation:
        if first_number == 0:
            first_number = float(input("What's the first number?: "))
        for sign in operations:
            print(f"{sign}\n")
        operation = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))
        result = calculate_result(operation, first_number, second_number)
        option = input(
            f"Type 'y' to continue calculting with {result}, type 'e' to exit the program or any key to start a new calculation: "
        )
        if option == "y":
            first_number = result
        elif option == "e":
            break
        else:
            first_number = 0
            os.system("cls")
            calculator()


calculator()
