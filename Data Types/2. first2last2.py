#python program to get a string made of the first 2 and last 2
#chars from a given string

def string(str):
    if len(str) < 2:
        return ''
    
    return str[0:2] + str[-2:]

print(string('Python'))
print(string('Py'))
print(string('w'))