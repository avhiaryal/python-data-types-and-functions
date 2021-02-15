#python program to multiplies all the items in a list
def list_multiply(items):
    product = 1
    for x in items:
        product *= x
    return product
print(list_multiply([1,2,3,4,5]))