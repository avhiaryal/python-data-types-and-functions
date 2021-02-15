#python program to sum all the items in a list
def list_sum(items):
    sum = 0
    for x in items:
        sum += x
    return sum
print(list_sum([1,2,3,4,5]))