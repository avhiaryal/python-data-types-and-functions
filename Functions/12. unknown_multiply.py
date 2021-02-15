# python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
def mul(n):
    return lambda x:x*n
result = mul(5)
print (result(10))