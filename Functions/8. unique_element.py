#python function that takes a list and returns a new list with unique elements og the first list.

def list(l):
    a = []
    for x in l:
        if x not in a:
            a.append(x)
    return a 
print(list([1,2,3,3,3,3,4,5]))
