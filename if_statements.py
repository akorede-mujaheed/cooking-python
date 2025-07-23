x = 5
y = 7

x = 12
y = 13
z = 13
if x>y+z or y>x+z or z>x+y:
        print("is not a tringle")
elif x==y+z or y==x+z or z==x+y:
        print("degenerate tringle")
else:
        print("is a tringle")


if x % 2 ==0:
    print("x is even ")
else:
    print("x is odd ")


if x > 0:
    print('x is positive')

if x %3 == 0:
    print("x is even")
else:
    print("x is odd")

if x < y:
    print("x is less than y ")
elif x > y:
    print("x is greater than y")
else:
    print("x and y are equal")        

if 0 < x:
    if x <10:
        print("x is a positive single_digit number")

if 0< x and x < 10:
    print("x is a positive single_digits number")

def count_down(n):
    if n <= 0:
        print("blast off")
    else:
        print(n)
        count_down(n-3)

count_down(10)

def print_n_times(string, n):
    if n > 0:
        print(string)
        print_n_times(string, n-1)
    

print_n_times("spam", 4)


if x == y:
    print("x and y are equal")
else:
    if x < y:
        print("x is less than ")
    else:
        print("x is greater than y")

if 0 < x:
    if x < 10:
        print("x is a positive single_digit number")

if not x <=0 and not x >= 10:
    print("x is a positive single_digit number")


def countdown_by_two(n):
    if n == 0:
        print("blastoff")
    else:
        print(n)
        countdown_by_two(n-2)

countdown_by_two(10)


def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x 


print(absolute_value(4))


def absolute_value_wrong():
    if x < 0:
        return -x
    if x > 0:
        return x
    
# print(absolute_value_wrong())


def is_divisible(x, y):
    if x % y ==0:
        return True
    else:
        return False


print(is_divisible(6, 4))
print(is_divisible(6, 3))


def is_divisible(a, b):
    return a % b == 0
if is_divisible(6, 2):
    print("divisible")
else:
    print("not divisible")


if is_divisible(6, 2) == True:
    print("divisible")