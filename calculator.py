def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def power(a, b):
    return a ** b

def modulo(a, b):
    if (b == 0):
        return "Error: Division by zero is not allowed."
    return a % b

print(add(3, 5))
print(modulo(10, 3))