calculation_of_units = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_of_units} {name_of_unit}"
    

def validate_and_execute():
    try:
        user_input_number = int(num_of_days_element)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered a 0, please enter a valid positive number.")
        else:
            print("You entered a negative number. No conversion for you.")          
    except ValueError:
        print("Your input is not a valid number. Don't ruin my program!")


user_input = ""

while user_input != "exit":
    user_input = input("Hey user enter a number of days as a comma separated list.\n")
    list_of_days = user_input.split(", ")
    print(list_of_days)
    print(set(list_of_days))
    print(type(list_of_days))
    print(type(set(list_of_days)))
    set_days = set(user_input.split(", "))
    for num_of_days_element in set_days:
        print(num_of_days_element)
        validate_and_execute()
