# Old terminal calculator application made in a previous class.

# add function
def add(a, b):
    return a + b


# subtract function
def subtract(a, b):
    return a - b


# multiply function
def multiply(a, b):
    return a * b


# divide function
def divide(a, b):
    if b == 0:
        raise ValueError('Cannot divide by zero')
    return a / b


OPERATIONS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


# function to make the calculation based upon what operation was typed
def calculate(expression):
    tokens = expression.split()
    a = float(tokens[0])
    op = tokens[1]
    b = float(tokens[2])
    operation = OPERATIONS[op]
    return operation(a, b)


# prints result or catches error
if __name__ == '__main__':
    expression = input('Enter an arithmetic expression: ')
    try:
        result = calculate(expression)
        print(f'Result: {result}')
    except Exception as e:
        print(f'Error: {e}')
