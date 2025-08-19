def factorial(n):
    if n == 0:
        return 1
    else:
        return 0
    
print(factorial(0))


def factorial(n):
    if n == 0:
        return 1
    else:
        return 0
    
print(factorial(4))


def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        return n * recurse
    
print(factorial(4))


def fibonacci(n):
    if n == 0:
        return 0
    elif  n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

print(fibonacci(6))


def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        return n * recurse
    
# print(factorial(1.5))

def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        return n * recurse
    
print(isinstance(3, int))

def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        return n * recurse
    
print(isinstance(1.5, int))


    
def factorial(n):
    if not isinstance(n, int):
        print("factrial is only defined for integers.")
        return None
    elif n < 0:
        print("facrorial is not defined for negative numbers.")
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
factorial(-2)


def factorial(n):
    space = " " * (4 * n)
    print(space, "factorial", n)
    if n == 0:
        print(space, "returning 1")
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        print(space, "returning", result)
        return result 
    
factorial(4)
