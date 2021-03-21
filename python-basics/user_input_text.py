calculation_of_units = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_of_units} {name_of_unit}"
    elif num_of_days == 0:
        return "0 days will not be calculated."


def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        calculated_value = days_to_units(user_input_number)
        print(calculated_value)
    else:
        print("Your input number is not a valid positive number, don't ruin my program.")


user_input = input("Hey user enter a positive number.\n")
validate_and_execute()
