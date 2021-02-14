#python program to change a given string to a new where the first and last chars have been exchanged.
def exchange(str):
    return str[-1:] + str[1:-1] + str[:1]

print (exchange('workshop'))
print (exchange('2021'))
