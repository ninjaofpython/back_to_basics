from helper import validate_and_execute
user_input = ""

while user_input != "exit":
    user_input = input("Hey user enter a number of days and conversion unit.\n")
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    validate_and_execute()
    
