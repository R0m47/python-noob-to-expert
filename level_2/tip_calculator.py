print("Welcome to the tip calculator!")
bill_value = float(input("What was the total bill? "))
tip_percentage = int(
    input("How much tip would you like to give? 10, 12, or 15 percetage? ")
)
people = int(input("How many people to split the bill? "))
value_per_person = round((((1 + (tip_percentage / 100)) * bill_value) / people),2)
print(f"Each person should pay: ${value_per_person}")
