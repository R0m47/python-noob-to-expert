from calculator_art import logo


def calculate_result(sign, first_number, second_number):
    if sign == "+":
        result = first_number + second_number
    elif sign == "-":
        result = first_number - second_number
    elif sign == "*":
        result = first_number * second_number
    elif sign == "/":
        result = first_number / second_number
    print(f"{first_number} {sign} {second_number} = {result}")
    return result


operations = ["+", "-", "*", "/"]
print(logo)
continue_calculation = True
valid_inputs = False
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
        f"Type 'y' to continue calculting with {result}, or any else to start a new calculation: "
    )
    if option == "y":
        first_number = result
    else:
        first_number = 0
