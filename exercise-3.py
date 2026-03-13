# ============================================================================
# TODO: Simple calculator 

# Write a calc function. It takes three arguments. 
# The default value for the third argument is "multiply". 
# The first two arguments are values that are to be combined using the operation requested by the third argument, 
# a string that is one of the following `add`, `subtract`, `multiply`, `divide`, `modulo`, `int_divide` (for integer division) and `power`. 
# The function returns the result.
# ============================================================================

def calc(a, b, c ="multiply"):
    if c == 'add':
        return a + b
    elif c == 'subtract':
        return a - b
    elif c == 'divide':
        if b == 0:
            raise ZeroDivisionError("Denominator should not be zero")
        return a / b
    elif c == 'modulo':
        return a % b
    elif c == 'int_divide':
        if b == 0:
            raise ZeroDivisionError("Denominator should not be zero")
        return a // b
    elif c == 'power':
        return a ** b
    else:
        return a * b