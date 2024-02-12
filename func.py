def multiplyFunc(x):
    result = x * x
    return result

print(multiplyFunc(3))
print(multiplyFunc(5))
print(multiplyFunc(50))

def multiplyFunc(x,y):
    multiply = x * y
    add = x + y
    divide = y/x
    return multiply, add, divide

print(multiplyFunc(9,5))