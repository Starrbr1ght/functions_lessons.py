# # def tea_order(customer_name, tea_type, milk=None, sweetener=None):
# #     print(customer_name, "ordered a", tea_type, "tea")
# #     if milk!=None:
# #         print(" -add:", milk)
# #     if sweetener!=None:
# #                 print(" -add:", sweetener)

# # tea_order("alice", "chamomile")
# # tea_order("bob" , "black" , "oat")
# # tea_order("Tony", "black", "oat", "honey" )

# # def tea_order(customer_name, tea_type, *args): #aqn *arg allows for there to be items added in
# #     print(customer_name, "ordered a", tea_type, "tea")
# #     for arg in args: #you could rename args "extras", but just be sure to include for arg in ____
# #            print(" -add:", arg)

# # tea_order("alice", "chamomile")
# # tea_order("bob" , "black" , milk= "oat")
# # tea_order("Tony", "black", milk= "oat", sweetener= "honey" )

# def tea_order(customer_name, tea_type, **kwargs): #A **kwarg allows for collecting a lable as well instead of just the data
#     print(customer_name, "ordered a", tea_type, "tea")
#     for key, value in kwargs.items():
#          print("  -add", key, ":", value)

# tea_order("alice", "chamomile")
# tea_order("bob" , "black" , milk= "oat")
# tea_order("Tony", "black", milk= "oat", sweetener= "honey" )


# def tea_order(customer_name, tea_type,*args,  **kwargs): #adds in an item then adds in the new term/add onand the item associated with it. (args always comes first)
#     print(customer_name, "ordered a", tea_type, "tea")
#     for key, value in kwargs.items():
#          print("  -add", key, ":", value)

# # tea_order("alice", "chamomile")
# # tea_order("bob" , "black" , milk= "oat")
# tea_order("Tony", "black", "oat", sweetener= "honey" )

# def tea_order(customer_name, tea_type,*args,  **kwargs):
#     print(customer_name, "ordered a", tea_type, "tea")
#     for key, value in kwargs.items():
#          print("  -add", key, ":", value)

# eves_extras= {"milk": "almond", "sweetener": "sugar", "flavor": "lemon"}

# tea_order("eve", "green", **eves_extras)
# tea_order("Tony", "black", "oat", sweetener= "honey" )








# # Indefinite Arguments (*args) Practice #1
# # Create a function called sum_squares that takes any number of numeric arguments, and returns the sum of their values squared.

# # For example for the arguments sum_squares(1,2,3) it should return 14 (1+4+9).
# def sum_squares(*args):
#      total=0 #initialize total to 0
#      for num in args: #iterate through each argument
#           total+= num **2 #add the square of the number to total
#           #first time through loop: total= 0 1^2 = 1
#           #second time through the loop: total = 1 + 2^2=5

#           return total
# print(sum_squares(3, 6, 9)) 
# print(sum_squares(-1, -2, -3))

# # Indefinite Arguments (*args) Practice #2
# # Create a function called absolute_sum, which takes any number of arguments, and returns the sum of their absolute values (that is, it takes the non-negative values and adds them together, in other words, considers them all - negative and positive - as positive).
# def sum_squares(*args):
#      total=0 #initialize total to 0
#      for num in args: #iterate through each argument
#           total+= abs(num) #add the square of the number to total
#           #first time through loop: total= 0 1^2 = 1
#           #second time through the loop: total = 1 + 2^2=5

#           return total
# print(sum_squares(3, 6, 9)) 
# print(sum_squares(-1, -2, -3))

# Indefinite Arguments (*args) Practice #3
# Create a function called personal_numbers that receives, as its first argument, a name, and then an indefinite number of values.

# The function should return the following message:

# "{name}, the sum of your numbers is {sum_numbers}"
def personal_number(name, *args):
    sum_numbers= sum(args)

    return (f"{name}, the sum of your numbers is {sum_numbers}")
print(personal_number("bob", 1, 2, 3, 4, 5))