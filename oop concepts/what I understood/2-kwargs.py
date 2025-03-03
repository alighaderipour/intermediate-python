# kwargs is for positional argument
# kwargs is a dict

def user_details(**kwargs):
    return "{} is {}".format(kwargs["name"], kwargs["age"])

print(user_details(name="Kevin", age=19))

# -------------------------------------------------------------------------------
def pri_user_details(**kwargs):
    for key, val in kwargs.items():
        print("{} : {}".format(key, val))

pri_user_details(name="Kevin", age=19)

# -------------------------------------------------------------------------------

my_kwargs ={"name": "Kevin", "age":19}
pri_user_details(**my_kwargs)