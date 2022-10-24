def multiply(a=0, b=0):
    num = 0
    for x in range(b):
        num += a
    return num


function5_7 = multiply(5, 7)
print(function5_7)


def exponent(j=0, k=0):
    num_1 = j
    for x in range(k - 1):
        num_1 *= j
    return num_1


function2_6 = exponent(2, 6)
print(function2_6)


def square(c):
    c = multiply(c, c)

    return c


function7_multiply = square(7)
print(function7_multiply)
