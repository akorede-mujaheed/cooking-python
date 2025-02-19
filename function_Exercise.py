
 
def calc_diameter_of_circle(radius):
    print("The diameter is: ", 2 * radius  )

calc_diameter_of_circle(3)


def calc_radius_of_circle(diameter):
    print ("the radius is ", diameter /2 )


calc_radius_of_circle(6)


def sum_of_two_number(number1, number2):
    print("sum_of_two_number", number1 + number2)

sum_of_two_number(2,3)


def cube_root_of_a_number(number):
    print("cube root of a number",number**(1/3))

cube_root_of_a_number(8)


def sum_of_two_number(number1, number2):
    print("the sum of the number is ", number1 + number2 )

sum_of_two_number(9,8) 


def check_even_or_odd(integer):
    # step 1: collect value
    value = integer

    # step 2: check if remainder after divide by 2
    is_remainder = value%2 != 0

    # step 3: return if even or odd
    if(is_remainder):
        print(value, "is an odd number")
    else:
        print(value, "is an even nuber")

check_even_or_odd(8)


def sum_of_two_number(number1, number2):
    print("the sum of the number is ", number1 + number2 )

sum_of_two_number(9,8) 


def icrement(number, by):
    return number + by

print (icrement(2,8)) 


def icrement(number, by= 1):
    return number + by 

print (icrement(2)) 


def multipy(*numbers):
    total = 1
    for number in numbers: 
        total*=number
    return total

print(multipy(3,4,5,6))
 

def multiply(*numbers):
    for number in numbers:
        print(number)

multiply(2,2,3,4,5)


def fizz_buzz(input): 
    if (input % 3 ==0) and (input % 5 ==0):
        return "fizzbuzz"
    if input  % 3==0:
        return "fizz"
    if input %5==0: 
        return "buzz"
    return input
    

print(fizz_buzz(5))

