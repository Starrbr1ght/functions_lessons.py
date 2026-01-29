
# Indefinite Arguments (**kwargs) Practice #1
# Create a function called number_attributes that counts the number of parameters that are passed, and returns that number as the result.
def number_attributes(**kwargs):
  return len(kwargs)
parameter = number_attributes(a=1, b=2, c=3, d=4, e=5)
print(parameter)







# Indefinite Arguments (**kwargs) Practice #2
# Create a function called list_attributes that returns in the form of a list the values of the attributes given in the form of keywords. The function must expect to receive any number of arguments of this type.
def list_attributes(**kwargs):
  return list(kwargs.values())

values_list_1 = list_attributes(name="mother",number= 2, food= "cheeseitz")
print(values_list_1)









# Indefinite Arguments (**kwargs) Practice #3
# Create a function called describe_person, which takes his name as parameters and then an indeterminate number of arguments. This function should display on the screen:
def describe_person(name, **kwargs):
 for key, value in (kwargs):
   formatted_key = key.replace('_', ' ').title()
   print(f"{formatted_key}: {value}")
   return 
 describe_person(name="janice", age= 24, job="unemployed")
 print(describe_person)
# Characteristics of {name}:
# {argument_name}: {argument_value}
# {argument_name}: {argument_value}
# etc...
# For example:

# describe_person("Ash", eye_color="brown", hair_color="black")

# Will print to the screen:

# Characteristics of Ash:
# eye_color: brown
# hair_color: black