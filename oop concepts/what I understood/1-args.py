# args is positional argument
# args is a tuple
def sum_num(*args):
    print("these are args : {}".format(args))
    print("this is sum all arguemnts: {}".format(sum(args))) 

sum_num(1,2,3,4,56)
# -------------------------------------------------------------------------------
some_numbers = (10,22, 48)
sum_num(*some_numbers)
# -------------------------------------------------------------------------------
def display_info(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

display_info(1, 2, 3, name="Alice", age=30)
# -------------------------------------------------------------------------------
