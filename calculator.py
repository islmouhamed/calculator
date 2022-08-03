def calculator(a, b, operation):
   #test the input if it's a numbre
    if (a.isnumeric() & b.isnumeric()):
        #cast the inputs into float
        a = float(a)
        b = float(b)
        #test the operation
        if operation == "+":
            result = a + b
        elif operation == "-":
            result = a - b
        elif operation == "/":
            result = a / b
        elif operation == "*":
            result = a * b
        else:
            result = "Operations supported: add, subtract, divide, multiple only"
    #if its not a number send a message
    else:
        result = "Please enter a valid number"

    return result