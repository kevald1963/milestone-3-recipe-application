import math

# Sanity check to ensure the test module is working!
def test_checker():
    return 1

def string_to_boolean(boolean_string):
    if boolean_string == "True":
         return True
    elif boolean_string == "False":
         return False
    else:
         raise ValueError("Cannot convert {} to a boolean.".format(boolean_string))
   
def roundup_nearest_ten(x):
    return int(math.ceil(x / 10.0)) * 10

def roundup_nearest_one(x):
    return int(math.ceil(x))


