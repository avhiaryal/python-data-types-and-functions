#python function to multiply all the number in the list
def multiply(num):
    count = 1
    for x in num:
        count *= x
    return count
print (multiply((8,2,3,-1,7)))

        