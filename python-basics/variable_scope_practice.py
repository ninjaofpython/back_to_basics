calculation_of_units = 24
name_of_unit = "hours"

def days_to_units(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days * calculation_of_units} {name_of_unit}") 
    print(custom_message)

# Testing the scope of a variable, num_of_days in days_to_units() doesn't see
# num_of_days in scope_check probably held at different addresses in memory.
def scope_check(num_of_days):
    my_var = "Variable inside function"
    print(name_of_unit)
    print(num_of_days)
    print(my_var)

    
days_to_units(45.5, "Awesome!")
days_to_units(91.5, "Looks good!")
scope_check(20)
