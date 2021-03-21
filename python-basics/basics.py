calculation_of_units = 24
name_of_unit = "hours"

def days_to_units(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days * calculation_of_units} {name_of_unit}") 
    print(custom_message)



days_to_units(45.5, "Awesome!")
days_to_units(91.5, "Looks good!")
