#python program to add 'ing' at the end of a given string.
#if the given string already ends with 'ing' then add 'ly' instead.
#length should be 3

def string(str):
    length = len(str)
    if length > 2:
        if str[-3:]== 'ing':
            str += 'ly'
        else:
            str += 'ing'
    return str

print(string('abc'))
print(string('string'))
print(string('cd'))
