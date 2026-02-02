def multiply(a, b):
    """Multiply two numbers.""" 
    return a * b
def dividiton(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error"