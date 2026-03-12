# ============================================================================
# TODO: Use a For Loop with a Range 

#Create a function called repeat. 
# It takes two parameters, a string and a count, and returns a new string that is the old one repeated count times.
# ============================================================================

def repeat(str1, counter):
    repeated_string = ''
    for i in range(0, counter - 1):
        repeated_string += str1

    return repeated_string