''''
This is a test.
'''

def addition(x,y):
    return x + y

def subtraction(x,y):
    return x - y

def multiplication(x,y):
    return x * y

def division(x,y):
    return x // y

def exponents(x,y):
    return x ** y

def orderOfOps(x,y,z,a):
    sum = addition(x,y)
    remainder = subtraction(x,z)
    product = multiplication(z,a)
    dividend = division(x, z)
    power = exponents(y,a)
    sum = addition(sum, remainder)
    remainder = subtraction(dividend, product)
    sum = addition(sum, remainder)
    power = exponents(power, dividend)
    dividend = division(sum, power)
    return dividend if dividend > 100 else 0


if __name__ == "__main__":
    addition(1, 3)
    orderOfOps(1, 2, 100, 4)